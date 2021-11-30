# from abc import ABC, abstractmethod
from abc import abstractmethod
import random
from GameObjects.GameObjectInterface import GameObjectInterface
from GameObjects.Purse import Purse
from abc import ABC

class ParticipantInterface(GameObjectInterface, ABC):

    @abstractmethod
    def act(self):
        pass

