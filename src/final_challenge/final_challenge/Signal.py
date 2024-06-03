from ultralytics import YOLO
import rclpy
import cv2 as cv
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Float32
from cv_bridge import CvBridge

from yolo_msg.msg import InferenceResult
from yolo_msg.msg import Yolov8Inference

from signal_msg.msg import Signal

bridge = CvBridge

class Signal(Node):

    def __init__(self):
        super().__init__('Controller')
          
        self.model = YOLO('../model/finalEq52.pt')
        
        self.yolov8_inference = Yolov8Inference()
        self.signal_msg = Signal()
        self.light_msg = Float32()
        self.counter = 0
        self.old_value = 0

        self.old_value_light = 1
        self.value_light = 0
        self.counter2 = 0

        self.subscription = self.create_subscription(
            Image,
            '/video_source/raw',
            self.camera_callback,
            0.1)
        self.subscription

        self.yolov8_pub = self.create_publisher(Yolov8Inference, "/Yolov8_Inference", 1)
        self.signal_pub = self.create_publisher(Signal, "/signal", 1)
        self.light_pub = self.create_publisher(Float32, "/light", 1)
        
        self.get_logger().info('|Signal node successfully initialized|')


    def camera_callback(self, data):
        
        img = bridge.imgmsg_to_cv2(data, "bgr8")
        results = self.model(img)
        self.yolov8_inference.header.frame_id = "inference"
        self.yolov8_inference.header.stamp = self.get_clock().now().to_msg()

        for r in results:
            boxes = r.boxes
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

                if(confidence < 0.5 or (self.inference_result.top - self.inference_result.bottom) < 30):
                    self.counter = 0
                    continue

                if(self.inference_result.class_name == "stop"):
                    self.signal_msg.num = 1
                    self.signal_msg.name = 'stop sign'
                elif(self.inference_result.class_name == "workers"):
                    self.signal_msg.num = 2
                    self.signal_msg.name = 'workers sign'
                elif(self.inference_result.class_name == "left"):
                    self.signal_msg.num = 3
                    self.signal_msg.name = 'left sign'
                elif(self.inference_result.class_name == "straight"):
                    self.signal_msg.num = 4
                    self.signal_msg.name = 'straight sign'
                elif(self.inference_result.class_name == "rotonda"):
                    self.signal_msg.num = 5
                    self.signal_msg.name = 'roundabout sign'
                else:
                    self.signal_msg.num = 0
                    self.signal_msg.name = 'no signal'
                
                if(self.old_value == self.signal_msg.num):
                    self.counter += 1
                else:
                    self.counter = 0
                self.old_value = self.signal_msg.num

                if(self.counter >= 3):
                    self.signal_msg.reliability = confidence
                    self.signal_pub.publish(self.signal_msg)
                    #self.yolov8_pub.publish(self.yolov8_inference)
                    self.yolov8_inference.yolov8_inference.clear()
                    self.counter = 0

                if(self.inference_result.class_name == "red"):
                    self.value_light = 0
                elif(self.inference_result.class_name == "yellow"):
                    self.value_light = 0.5
                else:
                    self.value_light = 1

                if(self.old_value_light == self.value_light):
                    self.counter2 += 1
                else:
                    self.counter2 = 0
                self.old_value_light = self.value_light

                if(self.counter2 >= 3):
                    self.light_msg.data = self.value_light
                    self.light_pub.publish(self.light_msg)
                    self.counter2 = 0
        
def main(args=None):
    rclpy.init(args=args)
    cv_e = Signal()
    rclpy.spin(cv_e)
    cv_e.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()