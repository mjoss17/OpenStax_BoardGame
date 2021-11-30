from Message.MessageInterface import MessageInterface
from GameObjects.Board import Board

class MovementMsg(MessageInterface):

    def __init__(self, data):
        self.data = data
        self.checker = lambda x: isinstance(x, Board())

    def data(self):
        return self.data

