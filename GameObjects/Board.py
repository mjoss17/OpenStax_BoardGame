from GameObjects.GameObjectInterface import GameObjectInterface

class Board(GameObjectInterface):

    def processMessage(self, msg):
        # get the ok to use this message
        result = msg.checker(self)
        

        