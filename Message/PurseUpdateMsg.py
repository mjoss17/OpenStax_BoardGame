from Message.MessageInterface import MessageInterface


class PurseUpdateMsg(MessageInterface):

    def __init__(self, id, data):
        self.data = [id, data]

    def data(self):
        return self.data