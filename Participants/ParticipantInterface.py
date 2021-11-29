# from abc import ABC, abstractmethod
from abc import abstractmethod
import random
from attributes.Purse import Purse

class ParticipantInterface:

    def __init__(self, name):
        self.name = name

    def act(self):
        pass

