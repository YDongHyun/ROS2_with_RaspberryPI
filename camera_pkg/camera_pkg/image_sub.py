import rclpy
import cv2
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class Image_sub(Node):
    def __init__(self):
        super().__init__('image_sub')
        self.image_sub=self.create_subscription(CompressedImage,'/CompressedImage',self.sub_callback,10)
        self.publisher = self.create_publisher(Image,'/video_image',10)   
        self.cv_bridge = CvBridge()
        self.image_sub

    def sub_callback(self,msg):
        global img
        img=self.cv_bridge.compressed_imgmsg_to_cv2(msg)

    def image_publisher(self):
        msg=Image()
        msg=self.cv_bridge.cv2_to_imgmsg(img)
        self.publisher.publish(msg)
        print("published")

def main(args=None):
    rclpy.init(args=args)
    node=Image_sub()
    try:
        while(1):
            node()
            node.image_publisher()
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')

    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
    main()
