import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32

class My_Publisher(Node) :
    def __init__(self) :
        super().__init__('Controller')
        
        #create publishers
        self.vel = self.create_publisher(Twist, '/cmd_vel', 10) #change car velocity

        #create subscribers
        self.subErrorCenter = self.create_subscription(Int32, "/center_error", self.timer_callback_errorCenter, 10) #receive current error between bottom point and screen center
        self.subErrorPoint = self.create_subscription(Int32, "/point_error", self.timer_callback_errorPoint, 10) #receive current error between points


        #create timers        
        self.timer_period_controller = 0.1 #callback time
        self.timer_controller = self.create_timer(self.timer_period_controller, self.timer_callback_controller) #logic goes in this timer
        self.get_logger().info('|Controller node successfully initialized|')

        #create different messsage types 
        self.msg_vel = Twist()       
        self.errorPoints = 0
        self.errorCenter = 0

        #create and initialize variables
        self.integral = 0  
        self.previouserror = 0
        self.integral = 0

        self.kp = 0.004 #0.4535
        self.ki = 0 #0.0531
        self.kd = 0 #0.3597


    
    def timer_callback_controller(self) :

        self.msg_vel.linear.x = 0.06
        # check first error with bottom point with center and then error between points
        if (self.errorCenter < 5 and self.errorCenter > -5):
            self.error = self.errorPoints
            if (self.errorPoints < 5 and self.errorPoints > -5):
                self.error = 0
            else:
                self.msg_vel.linear.x = 0.03
                self.vel.publish(self.msg_vel)
        else:
            self.error = self.errorCenter
            self.msg_vel.linear.x = 0.03

        #pid controller (pid = kp*proportional + ki*integral + kd*derivative)
        self.proportional = self.error
        self.integral = self.integral + (self.error * self.timer_period_controller)
        self.derivative = (self.error - self.previouserror) / self.timer_period_controller
        self.previouserror = self.error
        self.pid = (self.kp * self.proportional) + (self.ki * self.integral) + (self.kd * self.derivative)

        #set a limit in case the pid value surpasses the max velocity on the car
        if (self.pid > 0.035) :
            self.msg_vel.angular.z = 0.035
        elif (self.pid < -0.035) :
            self.msg_vel.angular.z = -0.035
        else: 
            self.msg_vel.angular.z = self.pid

        self.vel.publish(self.msg_vel)

    # save variables from topic into local
    def timer_callback_errorCenter(self, msg) :
        self.errorCenter = msg.data * -1


    def timer_callback_errorPoint(self, msg) :
        self.errorPoints = msg.data * -1

        
def main(args=None):
    rclpy.init(args=args)
    m_p = My_Publisher()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()