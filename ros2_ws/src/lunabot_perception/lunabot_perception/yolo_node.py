import rclpy
from rclpy.node import Node
from ultralytics import YOLO
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ament_index_python.packages import get_package_share_directory
import cv2
import os

class YoloNode(Node):
    def __init__(self):
        super().__init__("yolo_node")

        # Get correct model path inside this package
        pkg_path = get_package_share_directory('lunabot_perception')
        MODEL_PATH = os.path.join(pkg_path, 'models', 'best.pt')

        self.get_logger().info(f"Loading YOLO model from: {MODEL_PATH}")

        # Load YOLO model
        self.model = YOLO(MODEL_PATH)

        # Bridge for converting ROS → OpenCV
        self.bridge = CvBridge()

        # Subscribe to camera
        self.subscription = self.create_subscription(
            Image,
            '/rgb_camera_sensor/image_raw',
            self.image_callback,
            10
        )

        self.get_logger().info("YOLO node initialized and camera subscribed.")

    def image_callback(self, msg):
        try:
            frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        except Exception as e:
            self.get_logger().error(f"CV bridge error: {e}")
            return

        # Run YOLO on the frame
        results = self.model(frame)

        for r in results:
            if r.boxes is None:
                continue

            for box in r.boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                cls_name = self.model.names[cls_id]
                self.get_logger().info(f"Detected {cls_name} ({conf:.2f})")

def main(args=None):
    rclpy.init(args=args)
    node = YoloNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
