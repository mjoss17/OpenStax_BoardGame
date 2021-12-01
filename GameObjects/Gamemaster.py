from GameObjects.ParticipantInterface import ParticipantInterface

"""
GameMaser - Implements GameObjectInterface, and ParticipantInterface

GameMasters are participants and can use a turn to make actions, but are different 
than Players. They can be automated to do all sorts of things. 
"""
class GameMaster(ParticipantInterface):

    def __init__(self):
        pass

    def processMessage(self, msg):
        result = msg.checker(self)
        pass
    
    def act(self):
        return "Nothing to do"