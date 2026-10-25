import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CVIntegrationNode(Node):
    def __init__(self):
        super().__init__('cv_integration_node')
        
        
        self.subscription = self.create_subscription(
            Image,
            '/bcr_bot/kinect_camera/image_raw',
            self.image_callback,
            10)
            
        
        self.bridge = CvBridge()
        self.get_logger().info("OpenCV Integration Node Started!")

    def image_callback(self, msg):
        try:
            
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            
            
            cv2.imshow("Robot Eyes (OpenCV Live Feed)", cv_image)
            
            
            cv2.waitKey(1)
            
        except Exception as e:
            self.get_logger().error(f"Failed to convert image: {str(e)}")

def main(args=None):
    rclpy.init(args=args)
    node = CVIntegrationNode()
    rclpy.spin(node)
    
    
    cv2.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
