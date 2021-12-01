# from abc import ABC, abstractmethod
from abc import abstractmethod
import random
from GameObjects.GameObjectInterface import GameObjectInterface
from abc import ABC

"""
ParticipantInterface

Participants have the ability to act during a turn in the game. 
"""
class ParticipantInterface(GameObjectInterface, ABC):

    @abstractmethod
    def act(self):
        pass

