# test_publisher.py

import unittest
from clock_time.clock_publisher import get_time_message  # clock_publisherの関数をインポート

class TestClockPublisher(unittest.TestCase):
    def test_get_time_message(self):
        # get_time_message を呼び出し
        message = get_time_message()
        
        # epoch_time が float または int であれば通過する
        self.assertTrue(isinstance(message["epoch_time"], (float, int)))

if __name__ == "__main__":
    unittest.main()
