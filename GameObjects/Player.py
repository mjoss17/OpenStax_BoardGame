import random
import uuid

from GameObjects.ParticipantInterface import ParticipantInterface
from GameObjects.Purse import Purse
from Message.PurseUpdateMsg import PurseUpdateMsg
from Message.NextTurnMsg import NextTurnMsg
from Message.EmptyMsg import EmptyMsg


class Player(ParticipantInterface):
    
    # Players act by rolling
    rolling_range = 8;
    in_pentalty_box = False;
    purse = Purse()

    def __init__(self, name):
        self.name = str(name)
        self.uuid = uuid.uuid1()

    def name(self):
        return self.name

    def act(self):
        roll = random.randrange(self.rolling_range + 1)
        return roll

    def processMessage(self, msg):

        if isinstance(msg, PurseUpdateMsg):
            self.purse.add(1)
            return NextTurnMsg()
        else:
            return EmptyMsg()
