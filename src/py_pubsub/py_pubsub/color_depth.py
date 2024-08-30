import rclpy
import numpy as np
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from PIL import Image as im 
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

class PictureTest(Node):
    def __init__(self):
        super().__init__('hello_node')

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        self.image_subscription = self.create_subscription(
            Image,
            "/camera/camera/color/image_raw",
            self.image_callback,
            qos_profile
        )

        self.depth_subscription = self.create_subscription(
            Image,
            '/camera/camera/aligned_depth_to_color/image_raw',
            self.depth_callback,
            10)
        self.bridge = CvBridge()

        self.curr_image = None

    def image_callback(self, msg):
        self.get_logger().info('Received an image!')
        try:
        # Convert your ROS Image message to OpenCV2
            cv2_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError as e:
            #log out e
            self.get_logger().info(e)
        else:
            # Save your OpenCV2 image as a jpeg 
            cv2.imwrite('camera_image.jpeg', cv2_img)

    def depth_callback(self, msg):
        self.get_logger().info('Received a depth image!')
        
        try:
        # Convert your ROS Image message to OpenCV2
            depth_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
            depth_vis = cv2.normalize(depth_image, None, 0, 255, cv2.NORM_MINMAX)
            depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.2), cv2.COLORMAP_JET)
            cv2.imwrite('depth_image.tif', depth_image)
            cv2.imwrite('depth_vis.jpeg', depth_vis)
            cv2.imwrite('depth_colormap.jpeg', depth_colormap)
            depth_array = np.array(depth_image, dtype=np.float32)
            center_x = depth_array.shape[1] // 2
            center_y = depth_array.shape[0] // 2
            center_value = depth_array[center_y, center_x]
            self.get_logger().info(f"{center_value}")
        except CvBridgeError as e:
            #log out e
            self.get_logger().info(e)
        else:
            # Save your OpenCV2 image as a jpeg 
            pass


def main(args=None):
    rclpy.init(args=args)
    node = PictureTest()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
