import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import numpy as np


class CameraMockNode(Node):
    def __init__(self):
        super().__init__("camera_mock")
        self.pub = self.create_publisher(Image, "/image_raw", 10)
        self.timer = self.create_timer(1.0 / 30.0, self.publish_image)

        self.width = 640
        self.height = 480
        self.frame_id = "camera_frame"
        self.counter = 0

        self.get_logger().info("Camera mock node started, publishing to /image_raw")

    def publish_image(self):
        # Immagine RGB sintetica animata
        img = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        img[:, :, 0] = (self.counter * 5) % 255
        img[:, :, 1] = np.linspace(0, 255, self.width, dtype=np.uint8)
        img[:, :, 2] = np.linspace(0, 255, self.height, dtype=np.uint8)[:, None]

        msg = Image()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = self.frame_id
        msg.height = self.height
        msg.width = self.width
        msg.encoding = "rgb8"
        msg.is_bigendian = False
        msg.step = self.width * 3
        msg.data = img.tobytes()

        self.pub.publish(msg)
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = CameraMockNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()