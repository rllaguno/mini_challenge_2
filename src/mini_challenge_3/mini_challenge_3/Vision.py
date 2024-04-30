import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import String


class Vision(Node):
    def __init__(self):
        super().__init__('Vision')
        
        self.img = np.ndarray((720, 1280, 3))
        # Sets the color range of Red, Yellow, and Green
        self.lower_red = np.array([167,100,100])
        self.upper_red = np.array([187,255 ,255])
        self.lower_yellow = np.array([15,100,70])
        # self.upper_yellow = np.array([30,255, 255])
        self.upper_yellow = np.array([63,255, 255])
        self.lower_green = np.array([40, 40, 40])
        self.upper_green = np.array([85, 255, 255])

        self.valid_img = False
        self.bridge = CvBridge()
        self.counter_red = 0
        self.counter_yellow = 0
        self.counter_green = 0
        self.msg_color = String()
        # Subscribes to the camera image and publishes the processed images
        self.sub = self.create_subscription(Image, '/image_raw', self.camera_callback, 10)
        self.image_pub = self.create_publisher(Image, '/img_processing/color', 10)
        self.color_pub = self.create_publisher(String, '/color_id', 10)
        dt = 0.1
        self.timer = self.create_timer(dt, self.timer_callback)
        self.get_logger().info('Vision Node started')

    def camera_callback(self, msg):
        try:
            self.img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            self.valid_img = True
        except Exception as e:
            self.get_logger().info(f'Failed to get an image: {e}')

    def filter(self, hsvFrame, lower, upper):
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
                    if red_area > 2000:
                        cv2.drawContours(self.img, [red_contour], -1, (0, 0, 255), 2)
                        self.counter_red += 1  
                        self.counter_yellow = 0
                        self.counter_green = 0
                        print("ROJO: ", self.counter_red)

                for green_contour in green_contours:
                    green_area = cv2.contourArea(green_contour)
                    if green_area > 2000:
                        cv2.drawContours(self.img, [green_contour], -1, (0, 255, 0), 2)
                        self.counter_green += 1
                        self.counter_red = 0
                        self.counter_yellow = 0
                
                for yellow_contour in yellow_contours:
                    yellow_area = cv2.contourArea(yellow_contour)
                    if yellow_area > 2000:
                        cv2.drawContours(self.img, [yellow_contour], -1, (0, 255, 255), 2)
                        self.counter_yellow += 1
                        self.counter_red = 0
                        self.counter_green = 0
                
                if(self.counter_red >= 10):
                    self.msg_color.data = "RED"
                    self.color_pub.publish(self.msg_color)
                elif(self.counter_green >= 10):
                    self.msg_color.data = "GREEN"
                    self.color_pub.publish(self.msg_color)
                elif(self.counter_yellow >= 10):
                    self.msg_color.data = "YELLOW"
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
