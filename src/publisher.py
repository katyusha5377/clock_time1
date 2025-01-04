import time
from datetime import datetime

class ClockPublisher:
    """Publishes useful time information."""
    
    def __init__(self):
        self.running = True

    def get_time_message(self):
        now = datetime.now()
        return {
            "current_time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "epoch_time": time.time(),
        }

    def start(self):
        print("ClockPublisher is running...")
        while self.running:
            message = self.get_time_message()
            # トピックのような出力
            print(f"Published: {message}")
            time.sleep(1)

    def stop(self):
        self.running = False

if __name__ == "__main__":
    publisher = ClockPublisher()
    try:
        publisher.start()
    except KeyboardInterrupt:
        publisher.stop()
        print("\nClockPublisher stopped.")
