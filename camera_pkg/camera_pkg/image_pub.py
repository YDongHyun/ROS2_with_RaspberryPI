
import rclpy
import cv2
from rclpy.node import Node
from rclpy.qos import QoSProfile
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class Image_pub(Node):
    def __init__(self):
        super().__init__('image_pub')
        qos_profile = QoSProfile(depth=10)
        self.image_pub=self.create_publisher(Image,'/image',qos_profile)
        self.img_data = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
        self.cv_bridge = CvBridge()
        self.timer = self.create_timer(0.1,self.publish_image_msg)

    def publish_image_msg(self):
        msg=Image()
        msg=self.cv_bridge.cv2_to_imgmsg(self.img_data)
        self.image_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node=Image_pub()
    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')

    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
    main()
