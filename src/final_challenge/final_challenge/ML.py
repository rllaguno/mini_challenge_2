from ultralytics import YOLO
import rclpy
import cv2 as cv
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Float32, Int32
from cv_bridge import CvBridge

from yolo_msg.msg import InferenceResult
from yolo_msg.msg import Yolov8Inference

from signal_msg.msg import Signal

class ML(Node):

    def __init__(self):
        super().__init__('ML')
          
        self.model = YOLO('/home/puzzlebot/github/mini_challenges_eq5/src/final_challenge/model/bestEq53.pt')
        
        self.bridge = CvBridge()
        self.yolov8_inference = Yolov8Inference()
        self.signal_msg = Int32()
        self.light_msg = Float32()
        self.counter = [0, 0, 0]
        self.old_value = [8, 8, 8]
        self.c = 0

        self.old_value_light = 1.0
        self.value_light = 0.0
        self.counter2 = 0

        self.subscription = self.create_subscription(
            Image,
            '/video_source/raw',
            self.camera_callback,
            1)
        self.subscription
        
        self.yolov8_pub = self.create_publisher(Yolov8Inference, "/Yolov8_Inference", 1)
        self.signal_pub = self.create_publisher(Int32, "/signal", 1)
        self.light_pub = self.create_publisher(Float32, "/light", 1)
        self.img_pub = self.create_publisher(Image, "/inference_result", 1)
        
        self.get_logger().info('|ML node successfully initialized|')


    def camera_callback(self, data):
        
        img = self.bridge.imgmsg_to_cv2(data, "bgr8")
        results = self.model(img)
        self.yolov8_inference.header.frame_id = "inference"
        self.yolov8_inference.header.stamp = self.get_clock().now().to_msg()

        for r in results:
            boxes = r.boxes
            if(not boxes):
                try:
                    self.signal_msg.data = 0
                    self.signal_pub.publish(self.signal_msg)
                    self.get_logger().info(f'Signal: {self.signal_msg.data}')
                except Exception as e:
                    self.get_logger().error(f'Error publishing: {e}')
            self.c = 0 
            for box in boxes:
                self.inference_result = InferenceResult()
                b = box.xyxy[0].to('cpu').detach().numpy().copy()  # get box coordinates in (top, left, bottom, right) format
                c = box.cls
                confidence = box.conf.item()
                self.inference_result.class_name = self.model.names[int(c)]
                self.inference_result.top = int(b[0])
                self.inference_result.left = int(b[1])
                self.inference_result.bottom = int(b[2])
                self.inference_result.right = int(b[3])
                self.yolov8_inference.yolov8_inference.append(self.inference_result)

                self.get_logger().info(f'Confidence: {confidence} | Distance: {self.inference_result.bottom - self.inference_result.top}')

                if(confidence < 0.1 or (self.inference_result.bottom - self.inference_result.top) < 10):
                    try:
                        self.counter[self.c] = 0
                        self.signal_msg.data = 0
                        self.signal_pub.publish(self.signal_msg)
                        self.get_logger().info(f'Signal: {self.signal_msg.data}')
                    except Exception as e:
                        self.get_logger().error(f'Error publishing: {e}')
                    continue

                if(self.inference_result.class_name == "stop"):
                    self.signal_msg.data = 1
                    #self.signal_msg.name = 'stop sign'
                elif(self.inference_result.class_name == "workers"):
                    self.signal_msg.data = 2
                    #self.signal_msg.name = 'workers sign'
                elif(self.inference_result.class_name == "left"):
                    self.signal_msg.data = 3
                    #self.signal_msg.name = 'left sign'
                elif(self.inference_result.class_name == "straight"):
                    self.signal_msg.data = 4
                    #self.signal_msg.name = 'straight sign'
                elif(self.inference_result.class_name == "rotonda"):
                    self.signal_msg.data = 5
                    #self.signal_msg.name = 'roundabout sign'
                else:
                    try:
                        self.signal_msg.data = 0
                        self.signal_pub.publish(self.signal_msg)
                        self.get_logger().info(f'Signal: {self.signal_msg.data}')
                    except Exception as e:
                        self.get_logger().error(f'Error publishing: {e}')
                
                if(int(self.old_value[self.c]) == int(self.signal_msg.data)):
                    self.counter[self.c] = self.counter[self.c] + 1
                else:
                    self.counter[self.c] = 0
                self.old_value[self.c] = self.signal_msg.data

                if(self.counter[self.c] >= 3):
                    annotated_frame = results[0].plot()
                    img_msg = self.bridge.cv2_to_imgmsg(annotated_frame, encoding='bgr8')

                    try:
                        self.img_pub.publish(img_msg)
                        self.signal_pub.publish(self.signal_msg)
                        self.yolov8_pub.publish(self.yolov8_inference)
                        self.yolov8_inference.yolov8_inference.clear()
                        self.get_logger().info(f'Signal: {self.signal_msg.data} | Image: {img_msg} | Inference: {self.yolov8_inference}')
                    except Exception as e:
                        self.get_logger().error(f'Error publishing: {e}')
                    self.counter = [0, 0, 0]
                self.c = self.c + 1
                
                if(self.inference_result.class_name == "red"):
                    self.value_light = 0.0
                elif(self.inference_result.class_name == "yellow"):
                    self.value_light = 0.5
                else:
                    self.value_light = 1.0

                if(self.old_value_light == self.value_light):
                    self.counter2 += 1
                else:
                    self.counter2 = 0
                self.old_value_light = self.value_light

                if(self.counter2 >= 3):
                    try:
                        self.light_msg.data = self.value_light
                        self.light_pub.publish(self.light_msg)
                        self.counter2 = 0
                        self.get_logger().info(f'Light: {self.light_msg.data}')
                    except Exception as e:
                        self.get_logger().error(f'Error publishing: {e}')


def main(args=None):
    rclpy.init(args=args)
    ml = ML()
    rclpy.spin(ml)
    ml.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
