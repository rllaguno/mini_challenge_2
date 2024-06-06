import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32
from std_msgs.msg import Float32
from signal_msg.msg import Signal
import time

class Controller(Node) :
    def __init__(self) :
        super().__init__('Controller')
        
        #create publishers
        self.vel = self.create_publisher(Twist, '/cmd_vel', 10) #change car velocity

        #create subscribers
        self.subErrorCenter = self.create_subscription(Int32, "/center_error", self.timer_callback_errorCenter, 10) #receive current error between bottom point and screen center
        self.subErrorPoint = self.create_subscription(Int32, "/point_error", self.timer_callback_errorPoint, 10) #receive current error between points
        self.subLight = self.create_subscription(Float32, "/light", self.timer_callback_light, 10) #receive current error between points
        self.subSignal = self.create_subscription(Int32, "/signal", self.timer_callback_signal, 1) #receive current error between points
        self.subStandby = self.create_subscription(Int32, "/standby", self.timer_callback_standby, 10) #receive current error between points


        #create timers        
        self.timer_period_controller = 0.1 #callback time
        self.timer_controller = self.create_timer(self.timer_period_controller, self.timer_callback_controller) #logic goes in this timer
        self.get_logger().info('|Controller node successfully initialized yayyy|')

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

        self.light_multiplier = 1.0
        self.signal_num = 0

        self.counter = 0
        self.multWorkers = 1.0

        self.banderaLeft = False
        self.banderaWorkers = False
        self.banderaRotonda = False
        self.banderaStop = False
        self.banderaStraight = False
        self.secondsOld  = 0

        self.banderaSignal = False
        self.bandera = False
        self.standby_num = 0


    def timer_callback_controller(self) :
        print(self.signal_num)
        
        
        if (self.standby_num == 1 and (not self.banderaSignal)):
            self.msg_vel.linear.x = 0.0
            self.msg_vel.angular.z = 0.0
            self.vel.publish(self.msg_vel)
            self.banderaSignal = True

        if (self.banderaSignal):
            #left
            if (self.signal_num == 3 and (not self.banderaLeft) and (not self.bandera)):
                print("inside left")
                self.secondsOld  = time.time()
                self.msg_vel.linear.x = 0.06
                self.msg_vel.angular.z = 0.04
                self.vel.publish(self.msg_vel)
                self.banderaLeft = True 
                print(self.banderaLeft)

            if ((self.banderaLeft) and ((time.time() - self.secondsOld) >= 6.5)):
                self.msg_vel.linear.x = 0.0
                self.msg_vel.angular.z = 0.0
                self.vel.publish(self.msg_vel)
                self.banderaLeft = False 
                self.banderaSignal = False

            #rotonda
            if (self.signal_num == 5 and (not self.banderaRotonda)):
                print("inside left")
                self.secondsOld  = time.time()
                self.msg_vel.linear.x = 0.06
                self.msg_vel.angular.z = -0.04
                self.vel.publish(self.msg_vel)
                self.banderaRotonda = True 
                print(self.banderaRotonda)

            if ((self.banderaRotonda) and ((time.time() - self.secondsOld) >= 6.5)): 
                self.msg_vel.linear.x = 0.0
                self.msg_vel.angular.z = 0.0
                self.vel.publish(self.msg_vel)
                self.banderaRotonda = False 
                self.banderaSignal = False
                self.bandera = True
        
            #stop 
            if (self.signal_num == 1 and (not self.banderaStop) and self.bandera):
                print("inside stop")
                self.secondsOld  = time.time()
                self.msg_vel.linear.x = 0.0
                self.vel.publish(self.msg_vel)
                self.banderaStop = True 
                print(self.banderaStop)

            if ((self.banderaStop) and ((time.time() - self.secondsOld) >= 5)):
                self.msg_vel.linear.x = 0.06
                self.vel.publish(self.msg_vel)

            if ((self.banderaStop) and ((time.time() - self.secondsOld) >= 12)):
                self.msg_vel.linear.x = 0.0
                self.msg_vel.angular.z = 0.0
                self.vel.publish(self.msg_vel)
                self.banderaStop = False 
                self.banderaSignal = False

            #straight
            if (self.signal_num == 4 and (not self.banderaStraight)):
                print("inside straight")
                self.secondsOld  = time.time()
                self.msg_vel.linear.x = 0.06
                self.msg_vel.angular.z = 0.0
                self.vel.publish(self.msg_vel)
                self.banderaStraight = True 
                print(self.banderaStraight)

            if ((self.banderaStraight) and ((time.time() - self.secondsOld) >= 7)):
                self.msg_vel.linear.x = 0.0
                self.msg_vel.angular.z = 0.0
                self.vel.publish(self.msg_vel)
                self.banderaStraight = False
                self.banderaSignal = False
        
        else :
            #workers
            if (self.signal_num == 2 and (not self.banderaWorkers)):
                print("inside straight")
                self.secondsOld  = time.time()
                self.msg_vel.linear.x = 0.03
                self.msg_vel.angular.z = 0.0
                self.vel.publish(self.msg_vel)
                self.banderaWorkers = True 
                print(self.banderaWorkers)

            if ((self.banderaWorkers) and ((time.time() - self.secondsOld) >= 10)):
                self.msg_vel.linear.x = 0.0
                self.msg_vel.angular.z = 0.0
                self.vel.publish(self.msg_vel)
                self.banderaWorkers = False  
        

            self.msg_vel.linear.x = 0.06 * self.light_multiplier  
            # check first error with bottom point with center and then error between points
            if (self.errorCenter < 20 and self.errorCenter > -20):
                self.error = self.errorPoints
                if (self.errorPoints < 20 and self.errorPoints > -20):
                    self.error = 0
                else:
                    self.msg_vel.linear.x = 0.03 * self.light_multiplier
                    self.vel.publish(self.msg_vel)
            else:
                self.error = self.errorCenter
                self.msg_vel.linear.x = 0.03 * self.light_multiplier

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
            print(self.pid)
            self.vel.publish(self.msg_vel)
    
    # save variables from topic into local
    def timer_callback_errorCenter(self, msg) :
        self.errorCenter = msg.data * -1 

    def timer_callback_errorPoint(self, msg) :
        self.errorPoints = msg.data * -1

    def timer_callback_light(self, msg) :
        self.light_multiplier = msg.data

    def timer_callback_signal(self, msg) :
        self.signal_num = msg.data

    def timer_callback_standby(self, msg) :
        self.standby_num = msg.data
        
def main(args=None):
    rclpy.init(args=args)
    m_p = Controller()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()