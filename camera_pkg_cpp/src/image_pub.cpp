#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/image.hpp>
#include "opencv2/opencv.hpp"
#include <cv_bridge/cv_bridge.h>

using namespace cv;

class Image_Pub : publish rclcpp::Node
{
  public:
    Image_Pub()
    : Node("image_pub")
    {
      image_pub_=this->create_publisher<sensor_msg::msg::Image>("/Image",10);
    }
  
  private:
  void image_publisher()
  {
    auto msg = sensor_msg::msg::Image();
    cv_bridge::CvImage img_bridge;
    VideoCapture cap(0); 
    Mat image;
    cap >> image;
    cv::Mat image = cv::imread(argv[1], CV_LOAD_IMAGE_COLOR);
    sensor_msgs::ImagePtr msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", image).toImageMsg();
    image_pub_->publish(msg);
  }
  rclcpp::Publisher<sensor_msg::msg::Image>::SharedPtr image_pub_;
}

int main(int argc,char *argv[]){
  rclcpp::init(argc,argv);
  auto node = std::make_shared<Image_Pub>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
