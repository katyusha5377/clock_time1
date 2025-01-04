import time

class ClockPublisher:
    def get_time_message(self):
        """Generate a message containing current time and epoch time."""
        return {
            "current_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "epoch_time": int(time.time())
        }

    def publish(self):
        """Simulate publishing the time message."""
        message = self.get_time_message()
        print(f"Publishing message: {message}")

if __name__ == "__main__":
    publisher = ClockPublisher()
    publisher.publish()
