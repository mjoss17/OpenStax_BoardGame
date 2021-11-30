from Message.MessageInterface import MessageInterface

class QuestionMsg(MessageInterface):

    def __init__(self, player_id, text, space_num):
        self.data = [player_id, text, space_num]

    def data(self):
        return self.data
