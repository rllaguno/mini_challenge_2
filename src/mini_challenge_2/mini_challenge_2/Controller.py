import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Pose2D, Point
import rclpy.qos
from std_msgs.msg import Int32, Bool
import math 

class My_Publisher(Node) :
    def __init__(self) :
        super().__init__('Controller')
        
        #create publishers
        self.vel = self.create_publisher(Twist, '/cmd_vel', 10) #change car velocity
        self.flag = self.create_publisher(Int32, '/flag', 10) #to "point generator" to send next point

        qos_profile = rclpy.qos.qos_profile_sensor_data #eliminate noise

        #create subscribers
        self.subPose = self.create_subscription(Pose2D, "/odom", self.timer_callback_odometry, qos_profile) #receive current position and angle
        self.subPoint = self.create_subscription(Point, "/Point", self.timer_callback_point, qos_profile) #receive desired point
        self.amount = self.create_subscription(Int32, "/Amount", self.timer_callback_amount, 10)

        #create timers        
        self.timer_period_controller = 0.1 #callback time
        self.timer_controller = self.create_timer(self.timer_period_controller, self.timer_callback_controller) #logic goes in this timer
        self.get_logger().info('|Controller node successfully initialized|')

        #create different messsage types        
        self.msg_vel = Twist()
        self.msg_pose = Pose2D()
        self.msg_point = Point()
        self.msg_flag = Int32()
        self.msg_bandera = Bool()

        #create and initialize variables
        self.flag_counter = 0
        self.bandera = False
        self.bandera2 = False
        self.newX = 500
        self.newY = 500

        self.integralDistance = 0  
        self.previousErrorDistance = 0
        self.integralAngle = 0
        self.previousErrorDAngle = 0

        self.msg_point.x = 0.0
        self.msg_point.y = 0.0

        self.flag_ang = True
        self.flag_vel = False

        ### Distance ###
        self.kpDistance = 0.4 #5.2536
        self.kiDistance =  0 #0.1922
        self.kdDistance = 0 #4.9357

        ### Angle ###
        self.kpAngle = 0.02 #0.4535
        self.kiAngle = 0 #0.0531
        self.kdAngle = 0 #0.3597

        self.amount = 0

    
    def timer_callback_controller(self) :
        
        #check if there ir a desired point yet, yes? start
        if (self.msg_point.x != 0 or self.msg_point.y != 0):
            self.bandera2 = True 

        #set desired points into new variables and set bandera to True, this to check if we have received new points
        if (self.bandera2):
            if ((self.newX != self.msg_point.x) or (self.newY != self.msg_point.y)):
                self.newX = self.msg_point.x 
                self.newY = self.msg_point.y
                self.bandera = True


        #### PID ANGLE ####

            angleTarget = 0
            #check to see in which quadrant the car needs to turn
            #1st quadrant
            if ((self.msg_point.x >= self.msg_pose.x) and (self.msg_point.y >= self.msg_pose.y)) :
                opuesto = self.msg_point.y - self.msg_pose.y
                adyacente = self.msg_point.x - self.msg_pose.x
                angleRadians = math.atan(opuesto/adyacente)
                angleTarget = math.degrees(angleRadians)

            #4th quadrant
            elif ((self.msg_point.x >= self.msg_pose.x) and (self.msg_point.y <= self.msg_pose.y)) :
                opuesto = self.msg_point.x - self.msg_pose.x
                adyacente = self.msg_pose.y - self.msg_point.y 
                angleRadians = math.atan(opuesto/adyacente)
                angleTarget = math.degrees(angleRadians) + 270

            #2nd quadrant
            elif ((self.msg_point.x <= self.msg_pose.x) and (self.msg_point.y >= self.msg_pose.y)) :
                opuesto = self.msg_pose.x - self.msg_point.x
                adyacente = self.msg_point.y - self.msg_pose.y
                angleRadians = math.atan(opuesto/adyacente)
                angleTarget = math.degrees(angleRadians) + 90

            #3rd quadrant
            elif ((self.msg_point.x <= self.msg_pose.x) and (self.msg_point.y <= self.msg_pose.y)) :
                opuesto = self.msg_pose.y - self.msg_point.y 
                adyacente = self.msg_pose.x - self.msg_point.x
                angleRadians = math.atan(opuesto/adyacente)
                angleTarget = math.degrees(angleRadians) + 180

            #find the error angle (target angle - current angle)
            self.errorAngle = angleTarget - self.msg_pose.theta 
            
            #to also work with negatives
            if (self.errorAngle > 180) :
                self.errorAngle = self.errorAngle - 360
            elif (self.errorAngle  < -180) :
                self.errorAngle = self.errorAngle + 360

            #add prints to check if the code is working and the car if moving correctly
            print("Angle target: " + str(angleTarget))
            print("Theta: " + str(self.msg_pose.theta ))
            print("Error angle: " + str(self.errorAngle))
            print("X: " + str(self.msg_pose.x))
            print("Y: " + str(self.msg_pose.y))
            print("pX: " + str(self.msg_point.x))
            print("pY: " + str(self.msg_point.y))
            
            ## p angle controller (p = kp*errorAngle) ##
            self.pidAngle = self.kpAngle * self.errorAngle

            #try implementing a pid later
            '''
            ## pid angle controller (pid = kp*proportional + ki*integral + kd*derivative) ##
            self.proportionalAngle = self.errorAngle
            self.integralAngle = self.integralAngle + (self.errorAngle * self.timer_period_controller)0
            self.derivativeAngle = (self.errorAngle - self.previousErrorAngle) / self.timer_period_controller
            self.previousErrorAngle = self.errorAngle
            self.pidAngle = (self.kpAngle * self.proportionalAngle) + (self.kiAngle * self.integralAngle) + (self.kdAngle * self.derivativeAngle)
            print("PID angle: " + str(self.pidAngle))
            '''

            #set a limit in case the pid value surpasses the max velocity on the car
            if (self.pidAngle > 0.1) :
                self.msg_vel.angular.z = 0.1
            elif (self.pidAngle < -0.1) :
                self.msg_vel.angular.z = -0.1
            elif (self.flag_counter > self.amount):
                self.msg_vel.angular.z = 0.0
                self.msg_vel.linear.x = 0
            else:
                self.msg_vel.angular.z = self.pidAngle

            #self.msg_vel.linear.x = 0.0 #since we are not checking the linear velocity, just in case set it to 0 
            self.vel.publish(self.msg_vel) #publish the values of linear and angular velocities
            print("Angular vel: " + str(self.msg_vel.angular.z)) 
            

            #### PID DISTANCE ####

            #find the error distance (sqrt( (xTarget^2 - xCurrent^2) + (yTarget^2 - yCurrent^2) ) )
            self.errorDistance = math.sqrt(pow(self.msg_point.x - self.msg_pose.x, 2) + pow(self.msg_point.y - self.msg_pose.y, 2))
            
            ## p distance controller (p = kp*errorDistance) ##
            self.pidDistance = self.kpDistance * self.errorDistance

            #try implementing a pid later
            '''
            ## pid distance controller (pid = kp*proportional + ki*integral + kd*derivative) ##
            self.proportionalDistance = self.errorDistance
            self.integralDistance = self.integralDistance + (self.errorDistance * self.timer_period_controller)
            self.derivativeDistance = (self.errorDistance - self.previousErrorDistance) / self.timer_period_controller
            self.previousErrorDistance = self.errorDistance
            self.pidDistance = (self.kpDistance * self.proportionalDistance) + (self.kiDistance * self.integralDistance) + (self.kdDistance * self.derivativeDistance)
            print("PID distance: " + str(self.pidDistance))
            '''

            #set a limit in case the pid value surpasses the max velocity on the car
            if (self.pidDistance > 0.13) :
                self.msg_vel.linear.x = 0.13
                if (self.flag_counter > self.amount):
                    self.msg_vel.angular.z = 0.0
                    self.msg_vel.linear.x = 0
            else :
                self.msg_vel.linear.x = self.pidDistance
                if (self.flag_counter > self.amount):
                    self.msg_vel.angular.z = 0.0
                    self.msg_vel.linear.x = 0

            self.vel.publish(self.msg_vel) #publish the values of linear and angular velocities

            #check to see if the error is small to then start checking the angle (we are checking the x and y individually, not distance in general)
            if ((self.msg_pose.x < self.msg_point.x + 0.2 and self.msg_pose.x > self.msg_point.x - 0.2) and (self.msg_pose.y < self.msg_point.y + 0.2  and self.msg_pose.y > self.msg_point.y - 0.2) and self.bandera) :
                self.flag_counter += 1 
                self.msg_flag.data = self.flag_counter
                self.flag.publish(self.msg_flag) #publish the flag counter to "point generator" for it to send the next target point 
                self.bandera = False

                if (self.flag_counter > self.amount):
                    self.msg_vel.angular.z = 0
                    self.msg_vel.linear.x = 0
                    self.bandera2 = False
                    self.vel.publish(self.msg_vel) 
        
    #save received variables of "odometry"    
    def timer_callback_odometry(self, msg) :
        self.msg_pose.x = msg.x
        self.msg_pose.y = msg.y
        self.msg_pose.theta = msg.theta
    
    #save received variables of "point generator" 
    def timer_callback_point(self, msg) :
        self.msg_point.x = msg.x
        self.msg_point.y = msg.y
        self.msg_point.z = msg.z

    def timer_callback_amount(self, msg) :
        self.amount = msg.data
        
        
def main(args=None):
    rclpy.init(args=args)
    m_p = My_Publisher()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()