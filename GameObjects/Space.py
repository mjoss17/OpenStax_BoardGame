from GameObjects.GameObjectInterface import GameObjectInterface
from Message.EmptyMsg import EmptyMsg

'''
Space - implements GameObjectInterface
Contains:
id, category, solution (to question)

Handles:

Emits:
EmptyMessage
'''
class Space(GameObjectInterface):

    def __init__(self, id, category, question = None, solution = 0):
        self.id = id
        self.category = category
        self.question = None
        self.solution = solution

    def processMessage(self, msg):
        return EmptyMsg()

    def get_question(self):
        return self.category

    def check_answer(self, answer):
        if self.solution == None:
            return True
        elif answer == self.solution:
            return True
        else:
            return False