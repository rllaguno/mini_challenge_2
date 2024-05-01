import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_msgs.msg import Int32, Bool
import rclpy.qos
import yaml

class My_Publisher(Node):
    def __init__(self):
        super().__init__('PointGenerator')
        self.declare_parameter('numfigure', 10)
        self.point = self.create_publisher(Point, '/Point', 10)
        self.amount = self.create_publisher(Int32, '/Amount', 10)
        
        self.timer_period_point_generator = 0.18
        self.timer_point_generator = self.create_timer(self.timer_period_point_generator, self.timer_callback_point)

        qos_profile = rclpy.qos.qos_profile_sensor_data
        self.flag = self.create_subscription(Int32, "/flag", self.timer_callback_flag, qos_profile)
        self.get_logger().info('|Point Generator node successfully initialized|')

        self.msg_point = Point()
        self.msg_amount = Int32()
        self.flag = 0
        self.figure = 10
        self.msg_point.z = 1.0     

        self.a = 0   


    def timer_callback_point(self):
        self.figure = self.get_parameter('numfigure').get_parameter_value().integer_value
        
        # Square = 1
        if self.figure == 1:
            self.a = 3
            self.msg_amount.data = self.a
            if self.flag == 0:
                self.msg_point.x = 1.0
                self.msg_point.y = 0.0

            elif self.flag == 1:
                self.msg_point.x = 1.0
                self.msg_point.y = 1.0

            elif self.flag == 2:
                self.msg_point.x = 0.0
                self.msg_point.y = 1.0

            elif self.flag == 3:
                self.msg_point.x = 0.0
                self.msg_point.y = 0.0


        # Hexagon = 2
        elif self.figure == 2:
            self.a = 5
            self.msg_amount.data = self.a
            if self.flag == 0:
                self.msg_point.x = 0.2
                self.msg_point.y = 0.5

            elif self.flag == 1:
                self.msg_point.x = 0.8
                self.msg_point.y = 0.5

            elif self.flag == 2:
                self.msg_point.x = 1.0
                self.msg_point.y = 0.0

            elif self.flag == 3:
                self.msg_point.x = 0.8
                self.msg_point.y = -0.5

            elif self.flag == 4:
                self.msg_point.x = 0.2
                self.msg_point.y = -0.5

            elif self.flag == 5:
                self.msg_point.x = 0.0
                self.msg_point.y = 0.0


        # Rhombus = 3
        elif self.figure == 3:
            self.a = 3
            self.msg_amount.data = self.a
            if self.flag == 0:
                self.msg_point.x = 0.5
                self.msg_point.y = 0.5

            elif self.flag == 1:
                self.msg_point.x = 1.0
                self.msg_point.y = 0.0

            elif self.flag == 2:
                self.msg_point.x = 0.5
                self.msg_point.y = -0.5

            elif self.flag == 3:
                self.msg_point.x = 0.0
                self.msg_point.y = 0.0


        # Triangle = 4
        elif self.figure == 4:
            self.a = 2
            self.msg_amount.data = self.a
            if self.flag == 0:
                self.msg_point.x = 1.0
                self.msg_point.y = 0.5

            elif self.flag == 1:
                self.msg_point.x = 0.0
                self.msg_point.y = 1.0

            elif self.flag == 2:
                self.msg_point.x = 0.0
                self.msg_point.y = 0.0

        else:
            self.msg_point.x = 0.0
            self.msg_point.y = 0.0

        # Publish Point
        self.amount.publish(self.msg_amount) 
        self.point.publish(self.msg_point)
    
    def timer_callback_flag(self, msg):
        self.flag = msg.data
        
def main(args=None):
    rclpy.init(args=args)
    m_p = My_Publisher()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
        main()