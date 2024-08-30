import rclpy
from rclpy.node import Node
from mavros_msgs.msg import PositionTarget

class SetPositionNode(Node):
    def __init__(self):
        super().__init__('set_position_node')
        self.publisher = self.create_publisher(PositionTarget, '/mavros/setpoint_raw/local', 10)

        # 创建一个 PositionTarget 消息
        msg = PositionTarget()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.coordinate_frame = PositionTarget.FRAME_LOCAL_NED
        msg.type_mask = 3576
        msg.velocity.x = 0.0
        msg.velocity.y = 0.0
        msg.velocity.z = 1.0
        msg.yaw_rate = 0.0

        # 发布消息
        self.publisher.publish(msg)
        self.get_logger().info('Published PositionTarget message')

def main():
    rclpy.init()
    node = SetPositionNode()
    rclpy.spin_once(node, timeout_sec=1)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
