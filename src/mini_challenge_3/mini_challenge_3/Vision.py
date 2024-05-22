import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import Float32


class Vision(Node):
    def __init__(self):
        super().__init__('Vision')
        
        self.img = np.ndarray((30, 40, 3))
        
        # Sets the color range of Red, Yellow, and Green
        self.lower_yellow = np.array([20, 10, 150])
        self.upper_yellow = np.array([40, 255, 255])

        self.lower_green = np.array([40, 50, 50])
        self.upper_green = np.array([100, 255, 255])

        self.lower_red = np.array([165,50,50])
        self.upper_red = np.array([180,255 ,255])

        #self.lower_red = np.array([100,20,160])
        #self.upper_red = np.array([190,255 ,255])

        self.valid_img = False
        self.bridge = CvBridge()
        self.counter_red = 0
        self.counter_yellow = 0
        self.counter_green = 0
        self.msg_color = Float32()
        # Subscribes to the camera image and publishes the processed images
        self.sub = self.create_subscription(Image, '/image_raw', self.camera_callback, 10)
        self.image_pub = self.create_publisher(Image, '/img_processing/color', 10)
        self.color_pub = self.create_publisher(Float32, '/color_id', 10)
        dt = 0.5
        self.timer = self.create_timer(dt, self.timer_callback)
        self.get_logger().info('Vision Node started')

    def camera_callback(self, msg):
        try:
            self.img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            self.valid_img = True
        except Exception as e:
            self.get_logger().info(f'Failed to get an image: {e}')

    def double_filter(self, hsvFrame, lower1, upper1, lower2, upper2):
        #hace dos veces el bitwise con dos upper y lower con color 
        #nos retorna el canny del filtro
        mask1 = cv2.inRange(hsvFrame, lower1, upper1)
        mask2= cv2.inRange(hsvFrame,lower2,upper2)
        mask= cv2.bitwise_and(mask1, mask2)
        detected_output = cv2.bitwise_and(self.img, self.img, mask=mask)
        gray = cv2.cvtColor(detected_output, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(gray, 5)
        canny = cv2.Canny(blur, 75, 250)
        return canny
    
    def filter(self, hsvFrame, lower, upper):
        #hace solo una vez el lower y upper del filtro
    
        mask = cv2.inRange(hsvFrame, lower, upper)
        detected_output = cv2.bitwise_and(self.img, self.img, mask=mask)
        gray = cv2.cvtColor(detected_output, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(gray, 5)
        canny = cv2.Canny(blur, 75, 250)
        return canny

    def timer_callback(self):
        try:
            if self.valid_img:
                hsvFrame = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

                red_canny = self.filter(hsvFrame, self.lower_red, self.upper_red)
                yellow_canny = self.filter(hsvFrame, self.lower_yellow, self.upper_yellow)
                green_canny = self.filter(hsvFrame, self.lower_green, self.upper_green)
                
                red_contours, _ = cv2.findContours(red_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                yellow_contours, _ = cv2.findContours(yellow_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                green_contours, _ = cv2.findContours(green_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for red_contour in red_contours:
                    red_area = cv2.contourArea(red_contour)
                    if red_area > 5000:
                        cv2.drawContours(self.img, [red_contour], -1, (0, 0, 255), 2)
                        self.counter_red += 1  
                        self.counter_yellow = 0
                        self.counter_green = 0

                for green_contour in green_contours:
                    green_area = cv2.contourArea(green_contour)
                    if green_area > 5000:
                        cv2.drawContours(self.img, [green_contour], -1, (0, 255, 0), 2)
                        self.counter_green += 1
                        self.counter_red = 0
                        self.counter_yellow = 0
                
                for yellow_contour in yellow_contours:
                    yellow_area = cv2.contourArea(yellow_contour)
                    if yellow_area > 5000:
                        cv2.drawContours(self.img, [yellow_contour], -1, (0, 255, 255), 2)
                        self.counter_yellow += 1
                        self.counter_red = 0
                        self.counter_green = 0
                
                if(self.counter_red >= 5):
                    self.msg_color.data = 0.0
                    print('SENT RED: ', self.counter_red)
                    self.color_pub.publish(self.msg_color)
                elif(self.counter_green >= 5):
                    self.msg_color.data = 1.0
                    print('SENT GREEN: ', self.counter_green)
                    self.color_pub.publish(self.msg_color)
                elif(self.counter_yellow >= 5):
                    self.msg_color.data = 0.5
                    print('SENT YELLOW: ', self.counter_yellow)
                    self.color_pub.publish(self.msg_color)
                
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