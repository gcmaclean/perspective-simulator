class MoodTracker:

    def __init__(self):
        self.total_change = 0
        self.entries = 0

    def update(self, change):
        self.total_change += change
        self.entries += 1

    def average(self):
        if self.entries == 0:
            return 0
        return self.total_change / self.entries