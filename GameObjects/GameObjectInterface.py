from abc import ABC

"""
GameObjectInterface

GameObjects must have the ability to process messages
"""
class GameObjectInterface(ABC):

    def processMessage(self, msg):
        pass
