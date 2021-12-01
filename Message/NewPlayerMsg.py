from Message.MessageInterface import MessageInterface

"""
NewPlayerMsg
Sent by the Game_Updated class, Received by the Board GameObject
"""
class NewPlayerMsg(MessageInterface):

    def __init__(self, data):
        self.data = data

    def data(self):
        return self.data