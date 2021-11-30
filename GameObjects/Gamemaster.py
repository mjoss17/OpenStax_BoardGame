from GameObjects.ParticipantInterface import ParticipantInterface

class GameMaster(ParticipantInterface):

    def __init__(self):
        pass

    def processMessage(self, msg):
        result = msg.checker(self)
        pass
    
    def act(self):
        return "Nothing to do"