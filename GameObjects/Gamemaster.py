from GameObjects.ParticipantInterface import ParticipantInterface

class GameMaster(ParticipantInterface):

    def processMessage(self, msg):
        result = msg.checker(self)
        pass