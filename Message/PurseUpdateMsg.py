from Message.MessageInterface import MessageInterface


class PurseUpdateMsg(MessageInterface):

    def __init__(self, data):
        self.data = data

    def data(self):
        return self.data