class Logger:

    def __init__(self):
        self.history = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.history or timestamp >= self.history[message]:
            self.history[message] = timestamp + 10
            return True
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
