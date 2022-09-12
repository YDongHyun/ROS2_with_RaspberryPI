
import rclpy
import cv2
from rclpy.node import Node
from rclpy.qos import QoSProfile
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class Image_sub(Node):
    def __init__(self):
        super().__init__('image_sub')
        qos_profile = QoSProfile(depth=10)
        self.image_sub=self.create_subscription(Image,'/image',self.sub_callback,10)
        self.cv_bridge = CvBridge()
        self.image_sub

    def sub_callback(self,msg):
        img=self.cv_bridge.imgmsg_to_cv2(msg)
        cv2.imshow("Cam", img)
        cv2.waitKey()
        cv2.destroyAllWindows()


def main(args=None):
    rclpy.init(args=args)
    node=Image_sub()
    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')

    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
    main()
