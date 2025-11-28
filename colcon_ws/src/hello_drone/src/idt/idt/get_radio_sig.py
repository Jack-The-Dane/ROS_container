import rclpy
from rclpy.node import Node
from rclpy.qos import ReliabilityPolicy, QoSProfile
from sensor_msgs.msg import NavSatFix
from mavros_msgs.msg import RadioStatus

class ros_node_class(Node):
    def __init__(self):
        super().__init__('get_radio_sig')

        # publishers

        # subscribers
        self.sub_radio_sig = self.create_subscription(
            RadioStatus,                             # message type
            '/mavros/radio_status',      # topic to subscribe to
            self.on_radio_msg,                # callback function
            QoSProfile(depth=10,reliability=ReliabilityPolicy.BEST_EFFORT)
        )

        # timers
        self.timer = self.create_timer(2, self.timer_update)
        self.radio_file = open("radio.csv", "w")
        self.radio_file.write("Timestamp, RSSI_dbm, REM_RSSI_dbm, RSSI, REM_RSSI, noise, REM_noise, rxerrors \n")

    def __del__(self):
        self.radio_file.close()
 
    def on_radio_msg(self, msg:RadioStatus):
        self.get_logger().info(f"Got message at time {msg.header.stamp.sec + (float(msg.header.stamp.nanosec)/(10**9))}, RSSI: {msg.rssi_dbm}, REM_RSSI: {msg.remrssi_dbm}, Noise: {msg.noise}, REM_noise: {msg.remnoise}, RX_errors: {msg.rxerrors}")
        s = f"{msg.header.stamp.sec + (float(msg.header.stamp.nanosec)/(10**9))}, {msg.rssi_dbm}, {msg.remrssi_dbm}, {msg.rssi}, {msg.remrssi}, {msg.noise}, {msg.remnoise}, {msg.rxerrors} \n"
        self.radio_file.write(s)

    def timer_update(self):
        self.get_logger().info('Timer update')

def main(args=None):
    rclpy.init(args=args)
    ros_node = ros_node_class()
    rclpy.spin(ros_node)

    ros_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
