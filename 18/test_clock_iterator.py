# test_clock_iterator.py

from clock_iterator import ClockIterator
from custom_test_framework import TestCase


class TestClockIterator(TestCase):
    def setUp(self):
        self.clock = ClockIterator()

    def test_midnight(self):
        time = next(self.clock)
        assert time == "00:00", "Midnight time does not match"

    def test_one_minute_after_midnight(self):
        next(self.clock)  # Increment to 00:01
        time = next(self.clock)
        assert time == "00:01", "One minute after midnight time does not match"

    def test_noon(self):
        for _ in range(60 * 12):  # Fast forward to 12:00
            time = next(self.clock)
        assert time == "12:00", "Noon time does not match"

    def test_over_midnight(self):
        for _ in range(60 * 24):  # Fast forward to 00:00 next day
            next(self.clock)
        time = next(self.clock)
        assert time == "00:01", "Time after midnight does not match"


# Run the tests
if __name__ == "__main__":
    tests = [TestClockIterator()]
    for test in tests:
        test.run()
