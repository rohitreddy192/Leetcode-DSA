class Logger:

    def __init__(self):
        self.msg_dict = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.msg_dict:
            prevTimestamp = self.msg_dict[message]
            if timestamp - prevTimestamp >= 10:
                self.msg_dict[message] = timestamp
                return True
            else:
                return False
        self.msg_dict[message] = timestamp
        return True