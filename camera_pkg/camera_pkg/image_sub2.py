import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 

class ImageSubscriber(Node):

  def __init__(self):

    super().__init__('image_subscriber')

    self.subscription = self.create_subscription(CompressedImage, 'video_frames',self.listener_callback, 10)
    self.publisher = self.create_publisher(Image,'/video_image',10)   
    self.subscription 
    self.br = CvBridge()
  
  def listener_callback(self, data):
    self.get_logger().info('Receiving video frame')
    current_frame = self.br.compressed_imgmsg_to_cv2(data)

    msg=Image()
    msg=self.br.cv2_to_imgmsg(current_frame)
    self.publisher.publish(msg)
    print("published")

def main(args=None):
  rclpy.init(args=args)
  image_subscriber = ImageSubscriber()
  rclpy.spin(image_subscriber)
  image_subscriber.destroy_node()
  rclpy.shutdown()
 
if __name__ == '__main__':
  main()
