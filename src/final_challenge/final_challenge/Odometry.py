import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
import rclpy.qos
from std_msgs.msg import Float32
import numpy as np

class Odometry(Node):

    def __init__(self):
        super().__init__('Odometry')
        
        #create publishers
        self.odom = self.create_publisher(Pose2D, '/odom', 10) #publish current position and angle
        
        qos_profile = rclpy.qos.qos_profile_sensor_data #eliminate noise

        #create subscribers
        self.subL = self.create_subscription(Float32, "/VelocityEncL", self.timer_callback_l, qos_profile) #receive angular velocity of left wheel
        self.subR = self.create_subscription(Float32, "/VelocityEncR", self.timer_callback_r, qos_profile) #receive angular velocity of right wheel
        
        #create timers
        self.timer_period_controller = 0.1 #callback time
        self.timer_controller = self.create_timer(self.timer_period_controller, self.timer_callback_odometry) #logic goes in this timer

        self.enable_logger = self.declare_parameter('enable_logger_odometry', False)

        #create and initialize variables
        self.r = 0.05
        self.l = 0.19
        self.left_velocity = 0.0
        self.right_velocity = 0.0
        self.msg_pose = Pose2D()
        self.msg_pose.theta = 0.0
        self.thetaTemp2 = 0.0
        self.msg_pose.x = 0.0
        self.msg_pose.y = 0.0

        self.get_logger().info('|Odometry node successfully initialized|')


    def timer_callback_odometry(self):
        self.enable_logger = self.get_parameter('enable_logger_odometry').value
        
        #calculate velocities
        self.velocity_angular = self.r * ( (self.left_velocity - self.right_velocity) / self.l ) #angular velocity (r * ( (wr-wl) / l) )
        self.velocity_linear = self.r * ( (self.left_velocity + self.right_velocity) / 2 ) #linear velocity (r * ( (wr+wl) / 2) )

        #calculate position
        self.thetaTemp2 = self.thetaTemp2 + (self.velocity_angular * self.timer_period_controller) *-1.15 #theta in radians
        self.msg_pose.theta = self.thetaTemp2 * 57.269 #theta in degrees
        self.msg_pose.x = self.msg_pose.x + (self.velocity_linear * self.timer_period_controller) * np.cos(self.thetaTemp2) #distance in x
        self.msg_pose.y = self.msg_pose.y + ( self.velocity_linear * self.timer_period_controller ) * np.sin(self.thetaTemp2) #distance in y

        #publish 2D pose to /odom topic
        try: 
            self.odom.publish(self.msg_pose)
            if(self.enable_logger):
                self.get_logger().info(f'Odometry: {self.msg_pose.data}')
        except Exception as e:
            self.get_logger().error(f'Error publishing: {e}')


    #save received variables of left encoder
    def timer_callback_l(self,msg):
        self.left_velocity = msg.data


    #save received variables of right encoder
    def timer_callback_r(self,msg):
        self.right_velocity = msg.data
        

def main(args=None):
    rclpy.init(args=args)
    o = Odometry()
    rclpy.spin(o)
    o.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
        main()