from GameObjects.GameObjectInterface import GameObjectInterface

class Space(GameObjectInterface):

    def __init__(self, num, category):
        self.num = num
        self.category = category

    def processMessage(self, msg):
        pass