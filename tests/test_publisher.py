import unittest
from src.publisher import ClockPublisher

class TestClockPublisher(unittest.TestCase):
    def setUp(self):
        self.publisher = ClockPublisher()

    def test_get_time_message(self):
        message = self.publisher.get_time_message()
        self.assertIn("current_time", message)
        self.assertIn("epoch_time", message)
        self.assertIsInstance(message["current_time"], str)
        self.assertIsInstance(message["epoch_time"], float)

if __name__ == '__main__':
    unittest.main()
