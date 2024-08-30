import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TwistStamped
from mavros_msgs.msg import PositionTarget
import sys


class TwistToTwistStampedNode(Node):

    def __init__(self):
        super().__init__('twist_to_twist_stamped_node')

        self.cmd_vel_subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback,
            10)

        self.twist_stamped_publisher = self.create_publisher(
            TwistStamped,
            '/ap/cmd_vel',
            10)
        
        self.position_target_publisher = self.create_publisher(
            PositionTarget,
            '/mavros/setpoint_raw/local',
            10)

    def cmd_vel_callback(self, msg):

        twist_stamped_msg = TwistStamped()

        twist_stamped_msg.header.stamp = self.get_clock().now().to_msg()
        twist_stamped_msg.header.frame_id = 'base_link'  
    
        twist_stamped_msg.twist = msg

        self.twist_stamped_publisher.publish(twist_stamped_msg)

    def cmd_vel_callback1(self, msg):
        position_target_msg = PositionTarget()
        position_target_msg.header.stamp = self.get_clock().now().to_msg()
        position_target_msg.coordinate_frame = PositionTarget.FRAME_BODY_NED
        # position_target_msg.type_mask = PositionTarget.IGNORE_PX | PositionTarget.IGNORE_PY | PositionTarget.IGNORE_PZ | \
        #                                 PositionTarget.IGNORE_VX | PositionTarget.IGNORE_VY | PositionTarget.IGNORE_VZ | \
        #                                 PositionTarget.IGNORE_AFZ | PositionTarget.IGNORE_YAW_RATE

        position_target_msg.velocity.x = msg.linear.x
        position_target_msg.velocity.y = msg.linear.y
        position_target_msg.velocity.z = msg.linear.z

        position_target_msg.yaw = msg.angular.z / 2
        position_target_msg.yaw_rate = msg.angular.z / 2  

        self.position_target_publisher.publish(position_target_msg)

def main(args=None):
    rclpy.init(args=args)

    node = TwistToTwistStampedNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main(sys.argv)

