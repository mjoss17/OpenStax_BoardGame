from Message.MessageInterface import MessageInterface

"""
AttributeUpdateMsg
Sent by Player and Board GameObjects, received by PlayerObjects
"""
class AttributeUpdateMsg(MessageInterface):

    def __init__(self, player_num, attribute, newVal):
        self.data = [player_num, attribute, newVal]

    def data(self):
        return self.data