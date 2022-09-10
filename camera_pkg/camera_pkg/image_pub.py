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
        self.cv_bridge = CvBridge()
        self.publish_image_msg()

    def publish_image_msg(self): 
        msg=Image()
        vid_data = cv2.VideoCapture('/dev/video0')
        vid_data.set(3,640)
        vid_data.set(4,480)
        while(vid_data.isOpened()):
            ret,image=vid_data.read()
            if ret:
                msg=self.cv_bridge.cv2_to_imgmsg(image)
                self.image_pub.publish(msg)
            else:
                break
        vid_data.releasae()

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

        rclpy.shutdown()

if __name__=='__main__':
    main()
