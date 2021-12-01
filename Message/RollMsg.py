from Message.MessageInterface import MessageInterface

"""
RollMsg
Sent by Board GameObjects received by Player GameObjects
"""
class RollMsg(MessageInterface):
    
    def __init__(self, player_id):
        self.data = player_id

    def data(self):
        return self.data