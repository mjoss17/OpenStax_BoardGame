from GameObjects.GameObjectInterface import GameObjectInterface
from Message.EmptyMsg import EmptyMsg

class Space(GameObjectInterface):

    def __init__(self, num, category):
        self.num = num
        self.category = category

    def processMessage(self, msg):
        return EmptyMsg()

    def get_question(self):
        return self.category

    def check_answer(self, answer):
        return True
        # if answer == 0:
        #     return True
        # else:
        #     return False