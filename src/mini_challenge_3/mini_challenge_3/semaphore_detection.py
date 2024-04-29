import rclpy
from rclpy.node import Node
import numpy as np
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import String


class ColorId(Node):
    def __init__(self):
        super().__init__('circle_id_node') 
        self.img = None
        self.bridge = CvBridge()
        self.lower_red = np.array([0, 100, 100])
        self.upper_red = np.array([10, 255, 255])
        self.lower_yellow = np.array([20, 100, 100])
        self.upper_yellow = np.array([30, 255, 255])
        self.lower_green = np.array([40, 40, 40])
        self.upper_green = np.array([80, 255, 255])
        dt = 0.1
        self.subscription = self.create_subscription(Image, '/image_raw', self.camera_callback, 10) #cambiar este topico a uno que esuche la camara de la respectiva compu
        self.timer = self.create_timer(dt, self.timer_callback)
        self.circle_id_pub = self.create_publisher(Image, '/image_processing/color_id', 10)
        self.color_id = self.create_publisher(String, '/color_id', 10)
        self.get_logger().info('Color identification node started!')

    def camera_callback(self, msg):
        try:
            self.img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            self.get_logger().info('Failed to convert image to CV2: %s' % str(e))

    def find_red(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.lower_red, self.upper_red)
        return mask

    def find_yellow(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.lower_yellow, self.upper_yellow)
        return mask

    def find_green(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.lower_green, self.upper_green)
        return mask

    def find_contours(self, frame, mask):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blurred, 75, 200)
        contours, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        return contours
    def publish_color(self, color):
        msg = String()
        msg.data = color
        self.color_id.publish(msg)

    def timer_callback(self):
        if self.img is None:
            return

        red_mask = self.find_red(self.img)
        #yellow_mask = self.find_yellow(self.img)
        # green_mask = self.find_green(self.img) # Uncomment for green detection

        # Detect circles using Hough Circle Transform
        red_circles = cv2.HoughCircles(red_mask, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
                                       param1=200, param2=30, minRadius=10, maxRadius=100)

        if red_circles is not None:
            red_circles = np.uint16(np.around(red_circles))
            for circle in red_circles[0, :]:
                center = (circle[0], circle[1])
                radius = circle[2]
                cv2.circle(self.img, center, radius, (0, 0, 255), 2)
                self.publish_color('RED')

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
