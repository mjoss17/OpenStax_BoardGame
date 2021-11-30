from Message.MessageInterface import MessageInterface

class RollMsg(MessageInterface):
    
    def __init__(self, player_id):
        self.data = player_id

    def data(self):
        return self.data