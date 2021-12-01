from Message.MessageInterface import MessageInterface

"""
ErrorMsg
Sent by any GameObject to stop the program
"""
class ErrorMsg(MessageInterface):
    
    def __init__(self, description):
        self.description = description
        print(description)