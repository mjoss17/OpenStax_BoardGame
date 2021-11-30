from Message.MessageInterface import MessageInterface

class ErrorMsg(MessageInterface):
    
    def __init__(self, description):
        self.description = description
        print(description)