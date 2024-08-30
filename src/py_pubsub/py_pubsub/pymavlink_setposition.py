import rclpy
from geometry_msgs.msg import Twist
from pymavlink import mavutil
from rclpy.node import Node
def cmd_vel_callback(msg, master):

    delta_x = msg.linear.x
    delta_y = msg.linear.y
    delta_z = msg.linear.z
    # angular_z = msg.angular.z

    msg = master.mav.set_position_target_local_ned_encode(
        time_boot_ms=0,  
        target_system=0,  
        target_component=0,  
        coordinate_frame=8,  
        type_mask=0,  
        x=delta_x*1.2, y=delta_y*1.2, z=delta_z*1.2, 
        vx=0, vy=0, vz=0,  
        afx=0, afy=0, afz=0,  
        yaw=-msg.angular.z/20, yaw_rate=-msg.angular.z/20)  

   
    master.mav.send(msg)

class MavControlNode(Node):

    def __init__(self):
        super().__init__('mav_control_node')

        self.master = mavutil.mavlink_connection('udpin:127.0.0.1:14551')
        self.master.wait_heartbeat()

        self.cmd_vel_subscriber = self.create_subscription(
            Twist, '/cmd_vel', self.cmd_vel_callback, 50)

    def cmd_vel_callback(self, msg):
        cmd_vel_callback(msg, self.master)

def main(args=None):
    rclpy.init(args=args)
    node = MavControlNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
