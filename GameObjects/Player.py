from GameObjects.ParticipantInterface import ParticipantInterface
import random
from GameObjects.Purse import Purse
from Message.PurseUpdateMsg import PurseUpdateMsg
from Message.EmptyMsg import EmptyMsg
from Message.NextTurnMsg import NextTurnMsg

class Player(ParticipantInterface):
    
    # Players act by rolling
    rolling_range = 8;
    purse = Purse()

    def __init__(self, name):
        self.name = name

    def name(self):
        return self.name

    def act(self):
        roll = random.randrange(self.rolling_range + 1)
        return roll

    def processMessage(self, msg):

        if isinstance(msg, PurseUpdateMsg):
            self.purse.exchange(1)
            return NextTurnMsg()
        else:
            return EmptyMsg()
