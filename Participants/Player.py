from ParticipantInterface import ParticipantInterface
import random
from attributes.Purse import Purse

class Player(ParticipantInterface):
    
    # Players act by rolling
    rolling_range = 8;

    def __init__(self, name):
        self.name = name
        self.purse = Purse()

    def act(self):
        roll = random.randrange(self.rolling_range + 1)
        return roll