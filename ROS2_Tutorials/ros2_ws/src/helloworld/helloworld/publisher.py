import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('Minimal_Publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5 #seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.get_clock().now().to_msg().sec 
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    Minimal_Publisher = MinimalPublisher()
    rclpy.spin(Minimal_Publisher)
    Minimal_Publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
