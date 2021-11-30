import random
import uuid

from GameObjects.ParticipantInterface import ParticipantInterface
from GameObjects.Purse import Purse
from Message.AttributeUpdateMsg import AttributeUpdateMsg
from Message.ErrorMsg import ErrorMsg
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
        self.uuid = uuid.uuid4()
        self.attributes = {"jail_status" : False}

    def name(self):
        return self.name

    def act(self):
        roll = random.randrange(self.rolling_range + 1)
        return roll

    def processMessage(self, msg):

        if isinstance(msg, PurseUpdateMsg):
            self.purse.add(msg.data)
            return NextTurnMsg()
        elif isinstance(msg, AttributeUpdateMsg):
            msg_player_id = msg.data[0]
            msg_attribute = msg.data[1] 
            msg_value = msg.data[2]
            if self.uuid != msg_player_id:
                return EmptyMsg()
            else:
                if msg_attribute in self.attributes.keys():
                    self.attributes[msg_attribute] = msg_value
                    return NextTurnMsg()
                else:
                    return ErrorMsg("Attribute Unavailiable")
        else:
            return EmptyMsg()
