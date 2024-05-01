'''
import rclpy
from rclpy.node import Node
import numpy as np
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import String


class ColorId(Node):
    def __init__(self):
        super().__init__('semapore_detection') 
        self.img = None
        self.bridge = CvBridge()
        
        # Sets the color range of Red, Yellow, and Green
        self.lower_red = np.array([167,100,100])
        self.upper_red = np.array([187,255 ,255])
        self.lower_yellow = np.array([15, 100, 70])
        self.upper_yellow = np.array([30, 255, 255])
        self.lower_green = np.array([40, 40, 40])
        self.upper_green = np.array([85, 255, 255])
        
        # Subscribes to the camera image and publishes the processed images
        dt = 0.5
        self.subscription = self.create_subscription(Image, '/image_raw', self.camera_callback, 10)
        self.timer = self.create_timer(dt, self.timer_callback)
        self.circle_id_pub = self.create_publisher(Image, '/image_processing/color_id', 10)
        self.color_id = self.create_publisher(String, '/color_id', 10)
        self.get_logger().info('Color identification node started!')

    def camera_callback(self, msg):
        try:
            # Converts the image to a CV2 format
            self.img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            self.get_logger().info('Failed to convert image to CV2: %s' % str(e))

    # Function to find colored circles (masks) in an image frame
    def find_mask(self, frame, color):
        if(color == 'red'):
            upper = self.upper_red
            lower = self.lower_red
        elif(color =='yellow'):
            upper = self.upper_yellow
            lower = self.lower_yellow
        elif (color== 'green'):
            upper = self.upper_green
            lower = self.lower_green
        
        # Converts the frame to the HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Creates a mask using the upper and lower bounds for the specified color
        mask = cv2.inRange(hsv, lower, upper)
        # Applies Gaussian blur to the mask to reduce noise
        gaussian = cv2.GaussianBlur(mask, (9, 9), 2)
        # Detect circles in the masked image using Hough Circle Transform
        circles = cv2.HoughCircles(gaussian, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=30, maxRadius=50)
        # circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=20, minRadius=20, maxRadius=50)
        return circles
    
    # Function that publishes the color name
    def publish_color(self, color):
        msg = String()
        msg.data = color
        self.color_id.publish(msg)
        
    # Function to process the image and detect colored circles
    def timer_callback(self):
        if self.img is None:
            return
        # Checks each color mask
        red_circles = self.find_mask(self.img, 'red')
        yellow_circles = self.find_mask(self.img, 'yellow')
        green_circles = self.find_mask(self.img, 'green')
        circles = None
        if red_circles is not None:
            circles = red_circles
            title = 'RED'
            bgr = [0, 0, 0]
        elif yellow_circles is not None:
            circles = yellow_circles
            title = 'YELLOW'
            bgr = [0, 0, 0]
        elif green_circles is not None:
            circles = green_circles
            title = 'GREEN'
            bgr = [0, 0, 0]
            
        if circles is not None:
            # Converts circles to integer coordinates
            circles = np.round(circles[0,:]).astype("int")
            # Iterates over detected circles
            for (x,y,r) in circles:
                # Draws a circle on the image
                cv2.circle(self.img, (x,y), r, (bgr[0], bgr[1], bgr[2]), 10)
                # Publishes the color name of the circle dete
                self.publish_color(title)

        # Publish the modified image
        try:
            self.circle_id_pub.publish(self.bridge.cv2_to_imgmsg(self.img, encoding='bgr8'))
        except Exception as e:
            self.get_logger().info('Failed to publish image: %s' % str(e))


def main(args=None):
    rclpy.init(args=args)
    c_id = ColorId()
    rclpy.spin(c_id)
    c_id.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
''' 
import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class Vision(Node):
    def __init__(self):
        super().__init__('Vision')
        
        self.img = np.ndarray((720, 1280, 3))
        # Sets the color range of Red, Yellow, and Green
        self.lower_red = np.array([167,100,100])
        self.upper_red = np.array([187,255 ,255])
        self.lower_yellow = np.array([15,100,70])
        self.upper_yellow = np.array([30,255, 255])
        self.lower_green = np.array([40, 40, 40])
        self.upper_green = np.array([85, 255, 255])

        self.valid_img = False
        self.bridge = CvBridge()
        # Subscribes to the camera image and publishes the processed images
        self.sub = self.create_subscription(Image, '/image_raw', self.camera_callback, 10)
        self.image_pub = self.create_publisher(Image, '/img_processing/color', 10)
        self.color_pub = self.create_publisher(String, '/color_id', 10)
        dt = 0.1
        self.timer = self.create_timer(dt, self.timer_callback)
        self.get_logger().info('CV Node started')

    def camera_callback(self, msg):
        try:
            self.img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            self.valid_img = True
        except Exception as e:
            self.get_logger().info(f'Failed to get an image: {e}')

    def timer_callback(self):
        try:
            if self.valid_img:
                hsvFrame = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
                
                # Detect red circles
                red_mask = cv2.inRange(hsvFrame, self.lower_red, self.upper_red)
                red_detected_output = cv2.bitwise_and(self.img, self.img, mask=red_mask)
                red_gray = cv2.cvtColor(red_detected_output, cv2.COLOR_BGR2GRAY)
                red_blur = cv2.medianBlur(red_gray, 5)
                red_canny = cv2.Canny(red_blur, 75, 250)
                red_contours, _ = cv2.findContours(red_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for red_contour in red_contours:
                    red_area = cv2.contourArea(red_contour)
                    if red_area > 2000:
                        cv2.drawContours(self.img, [red_contour], -1, (0, 0, 255), 2)
                
                # Detect green circles
                green_mask = cv2.inRange(hsvFrame, self.lower_green, self.upper_green)
                green_detected_output = cv2.bitwise_and(self.img, self.img, mask=green_mask)
                green_gray = cv2.cvtColor(green_detected_output, cv2.COLOR_BGR2GRAY)
                green_blur = cv2.medianBlur(green_gray, 5)
                green_canny = cv2.Canny(green_blur, 75, 250)
                green_contours, _ = cv2.findContours(green_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for green_contour in green_contours:
                    green_area = cv2.contourArea(green_contour)
                    if green_area > 2000:
                        cv2.drawContours(self.img, [green_contour], -1, (0, 255, 0), 2)
                
                # Detect yellow circles
                yellow_mask = cv2.inRange(hsvFrame, self.lower_yellow, self.upper_yellow)
                yellow_detected_output = cv2.bitwise_and(self.img, self.img, mask=yellow_mask)
                yellow_gray = cv2.cvtColor(yellow_detected_output, cv2.COLOR_BGR2GRAY)
                yellow_blur = cv2.medianBlur(yellow_gray, 5)
                yellow_canny = cv2.Canny(yellow_blur, 75, 250)
                yellow_contours, _ = cv2.findContours(yellow_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for yellow_contour in yellow_contours:
                    yellow_area = cv2.contourArea(yellow_contour)
                    if yellow_area > 2000:
                        cv2.drawContours(self.img, [yellow_contour], -1, (0, 255, 255), 2)

                self.image_pub.publish(self.bridge.cv2_to_imgmsg(self.img))
        except Exception as e:
            self.get_logger().info(f'Failed to process image: {e}')

def main(args=None):
    rclpy.init(args=args)
    cv_e = Vision()
    rclpy.spin(cv_e)
    cv_e.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()