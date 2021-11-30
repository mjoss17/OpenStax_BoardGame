from Message.MessageInterface import MessageInterface

class AnswerMsg(MessageInterface):

    def __init__(self, player_id, space_num, answer):
        self.data = [player_id, space_num, answer]

    def data(self):
        return self.data