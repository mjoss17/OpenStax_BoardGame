from Message.MessageInterface import MessageInterface

"""
MovementMsg
Sent by the Player GameObject, received by the Board GameObject
"""
class MovementMsg(MessageInterface):

    def __init__(self, player_num, distance):
        self.data = [player_num, distance]

    def data(self):
        return self.data

