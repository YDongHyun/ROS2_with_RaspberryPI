#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/CompreesedImage.hpp"

using namespace std::chrono_literals;

class Image_Pub : public rclcpp::Node
{
public:
  image_publisher()
  : Node("img_publisher"), count_(0)
  {
    publisher_ = this->create_publisher<std_msgs::msg::CompreesedImage>("/CompressedImage", 10);
  }

private:
  void publish_msg()
  {
    vid_data = VideoCapture capture(".\\video.avi");
    auto msg = std_msgs::msg::CompreesedImage();
    msg = 
    RCLCPP_INFO(this->get_logger(), "Published");
    publisher_->publish(msg);
  }
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  while (1){
    rclcpp::spin_once(std::make_shared<image_publisehr>());
    Image_pub.publish_msg();
  }
  rclcpp::shutdown();
  return 0;
}