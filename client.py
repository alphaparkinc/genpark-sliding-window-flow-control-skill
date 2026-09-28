"""Sliding Window Flow Control Protocol.
100% Python Standard Library.
"""

class SlidingWindowFlowControl:
    """TCP-style sliding window flow control with cumulative acknowledgment."""
    def __init__(self, window_size: int):
        self.window_size = window_size
        self.base = 0
        self.next_seq = 0
        self.buffer = {}
        self.acked = set()

    def send_packet(self, data: str) -> tuple:
        if self.next_seq < self.base + self.window_size:
            seq = self.next_seq
            self.buffer[seq] = data
            self.next_seq += 1
            return True, seq
        return False, None

    def receive_ack(self, ack_seq: int) -> int:
        if ack_seq in self.buffer:
            self.acked.add(ack_seq)
            while self.base in self.acked:
                del self.buffer[self.base]
                self.base += 1
        return self.base

    def get_state(self) -> dict:
        return {
            "window_size": self.window_size,
            "base": self.base,
            "next_seq": self.next_seq,
            "unacked_count": len(self.buffer),
            "in_flight": list(self.buffer.keys())
        }
