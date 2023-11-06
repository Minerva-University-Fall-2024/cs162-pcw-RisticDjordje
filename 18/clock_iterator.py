import time

class ClockIterator:
    def __init__(self):
        self.hours = 0
        self.minutes = 0

    def __iter__(self):
        return self

    def __next__(self):
        time_str = f"{self.hours:02d}:{self.minutes:02d}"
        self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        if self.hours == 24:
            self.hours = 0
        return time_str

# Example usage:
clock = ClockIterator()
while True:
    print(next(clock))
    time.sleep(60)  # Wait for one minute before the next iteration. 
