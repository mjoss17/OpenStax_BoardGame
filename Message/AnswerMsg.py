from Message.MessageInterface import MessageInterface

class AnswerMsg(MessageInterface):

    def __init__(self, space_num, answer):
        self.data = [space_num, answer]

    def data(self):
        return self.data