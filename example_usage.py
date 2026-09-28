from client import SlidingWindowFlowControl

def main():
    sw = SlidingWindowFlowControl(window_size=3)
    print("Send 0:", sw.send_packet("data_0"))
    print("Send 1:", sw.send_packet("data_1"))
    print("Send 2:", sw.send_packet("data_2"))
    print("Send 3 (fails, full window):", sw.send_packet("data_3"))
    print("ACK 0:", sw.receive_ack(0))
    print("Send 3 (succeeds now):", sw.send_packet("data_3"))
    print("Current State:", sw.get_state())

if __name__ == "__main__":
    main()
