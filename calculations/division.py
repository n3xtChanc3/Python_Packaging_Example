# division.py

class Division:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def divide(self):
        if self.y == 0:
            return "Error: Division by zero"
        return self.x / self.y
