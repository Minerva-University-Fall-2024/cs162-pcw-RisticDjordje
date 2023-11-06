import unittest
import time
from clock_iterator import ClockIterator

class TestClockIterator(unittest.TestCase):
    def test_iterator(self):
        clock = ClockIterator()
        expected_time = "00:00"
        
        for _ in range(60 * 24):  # Test for a full day (24 hours)
            self.assertEqual(next(clock), expected_time)
            # Increment the expected time manually
            if expected_time == "23:59":
                expected_time = "00:00"
            else:
                hours, minutes = map(int, expected_time.split(":"))
                if minutes == 59:
                    expected_time = f"{hours + 1:02d}:00"
                else:
                    expected_time = f"{hours:02d}:{minutes + 1:02d}"
            
    def test_endless_iterator(self):
        clock = ClockIterator()
        start_time = time.time()
        for _ in range(10):  # Test for 10 minutes
            next_time = next(clock)
            elapsed_time = time.time() - start_time
            expected_time = time.strftime("%H:%M", time.gmtime(elapsed_time))
            self.assertEqual(next_time, expected_time)
            time.sleep(60)  # Wait for one minute

if __name__ == '__main__':
    unittest.main()
