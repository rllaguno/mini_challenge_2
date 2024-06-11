import rclpy
import rclpy.qos
from rclpy.node import Node
import cv2 as cv
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import Int32

class Vision(Node):

    def __init__(self):
        super().__init__('Vision')
        
        self.img = None
        self.crop_pixels = 50
        self.valid_img = False
        self.bridge = CvBridge()
        self.ce_msg = Int32()
        self.pe_msg = Int32()
        self.standby_msg = Int32()
        self.standby_counter = 0

        qos_profile = rclpy.qos.qos_profile_sensor_data #eliminate noise

        # Subscribes to the camera image and publishes the processed images
        self.sub = self.create_subscription(Image, '/video_source/raw', self.camera_callback, qos_profile)
        self.center_error_pub = self.create_publisher(Int32, '/center_error', 10)
        self.points_error_pub = self.create_publisher(Int32, '/points_error', 10)
        self.standby_pub = self.create_publisher(Int32, '/standby', 10)
        self.frame_pub = self.create_publisher(Image, '/cv_image', 10)

        self.enable_logger = self.declare_parameter('enable_logger_vision', False)

        dt = 0.1
        self.timer = self.create_timer(dt, self.timer_callback)
        self.get_logger().info('|Vision Node successfully initialized|')


    def camera_callback(self, msg):
        try:
            self.img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            self.valid_img = True
        except Exception as e:
            self.get_logger().info(f'Failed to get an image: {e}')


    def timer_callback(self):
        self.enable_logger = self.get_parameter('enable_logger_vision').value

        try:
            if self.valid_img:
                
                #frame = self.img[:-self.crop_pixels, :]
                frame = self.img
                #frame = cv.resize(frame, (800, 600), interpolation=cv.INTER_LINEAR)

                # Apply median blur
                frame = cv.medianBlur(self.img, 5)

                # Convert to grayscale
                frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

                # Apply threshold
                _, frame = cv.threshold(frame, 90, 255, cv.THRESH_BINARY_INV)

                # Create a blank mask with the same height and width as the frame
                blank = np.zeros(frame.shape[:2], dtype='uint8')

                # Define the top-left and bottom-right coordinates of the rectangle
                top_left = (1 * frame.shape[1] // 4, frame.shape[0] // 2)
                bottom_right = (3 * frame.shape[1] // 4, frame.shape[0])

                # Draw a filled rectangle on the blank mask
                mask = cv.rectangle(blank, top_left, bottom_right, (255), thickness=cv.FILLED)

                # Apply the mask to the frame using bitwise_and
                frame = cv.bitwise_and(frame, frame, mask=mask)

                # Obtener los contours del frame
                contours, _ = cv.findContours(frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
                            
                if contours:
                    # Obtener el contour mas grande
                    largest_contour = max(contours, key=cv.contourArea)
                    largest_contour = np.squeeze(largest_contour)

                    if largest_contour.shape[0] < 12:
                        self.standby_counter = self.standby_counter + 1
                        if self.standby_counter >= 2:
                            self.standby_msg.data = 1
                            try:
                                self.standby_pub.publish(self.standby_msg)
                                if(self.enable_logger):
                                    self.get_logger().info(f'Standby: {self.standby_msg.data}')
                            except Exception as e:
                                self.get_logger().error(f'Error publishing: {e}')
                        return

                    # Si el contour es de 2 dimensiones y tiene 2 columnas
                    if largest_contour.ndim == 2 and largest_contour.shape[1] == 2:
                        # Obtener valor del punto mas bajo
                        bottom_y = largest_contour[:, 1].max()
                        bottom_contour = largest_contour[largest_contour[:, 1] == bottom_y]
                        bottom_x_center = bottom_contour[:, 0].mean()
                        bottom_point = (int(bottom_x_center), int(bottom_y))

                        # Obtener valor del punto mas alto
                        top_y = largest_contour[:, 1].min()
                        top_contour = largest_contour[largest_contour[:, 1] == top_y]
                        top_x_center = top_contour[:, 0].mean()
                        top_point = (int(top_x_center), int(top_y))

                        # Dibuja los puntos en el frame
                        cv.circle(frame, bottom_point, 1, (127), -1)
                        cv.circle(frame, top_point, 1, (127), -1)

                        # Calcula el centro del frame
                        centerX = frame.shape[1] // 2

                        # Calcula diferencias en pixeles entre los puntos y el centro del frame
                        bottom_position_diff = bottom_point[0] - centerX
                        top_position_diff = top_point[0] - centerX
                        position_diff_between_points = bottom_position_diff - top_position_diff

                        try:
                            self.ce_msg.data = bottom_position_diff
                            self.pe_msg.data = position_diff_between_points
                            self.center_error_pub.publish(self.ce_msg)
                            self.points_error_pub.publish(self.pe_msg)
                            self.standby_counter = 0
                            self.standby_msg.data = 0
                            self.standby_pub.publish(self.standby_msg)
                            self.frame_pub.publish(self.bridge.cv2_to_imgmsg(frame))
                            if(self.enable_logger):
                                self.get_logger().info(f'Center Error: {self.ce_msg.data} | Points Error: {self.pe_msg.data} | Standby: {self.standby_msg.data}')
                        except Exception as e:
                            self.get_logger().error(f'Error publishing: {e}')
                                                
                        self.valid_img = False

        except Exception as e:
            self.get_logger().info(f'Failed to process image: {e}')


def main(args=None):
    rclpy.init(args=args)
    cv_e = Vision()
    rclpy.spin(cv_e)
    cv_e.destroy_node()
    cv.destroyAllWindows()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
