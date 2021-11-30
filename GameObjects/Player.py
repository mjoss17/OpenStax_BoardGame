import random
import uuid

from GameObjects.ParticipantInterface import ParticipantInterface
from Message.AnswerMsg import AnswerMsg
from Message.AttributeUpdateMsg import AttributeUpdateMsg
from Message.ErrorMsg import ErrorMsg
from Message.NextTurnMsg import NextTurnMsg
from Message.EmptyMsg import EmptyMsg
from Message.QuestionMsg import QuestionMsg
from Message.RollMsg import RollMsg
from Message.MovementMsg import MovementMsg
from Message.GameOverMsg import GameOverMsg


class Player(ParticipantInterface):
    
    rolling_range = 8
    winning_count = 10

    def __init__(self, name):
        self.name = str(name)
        self.uuid = uuid.uuid4()
        self.attributes = {"jail_status" : False, "coins" : 0}

    def name(self):
        return self.name

    def act(self):
        roll = random.randrange(self.rolling_range + 1)
        self.check_attribute_updates(roll)
        return roll

    def check_attribute_updates(self, new_roll):
        if (new_roll % 2 != 0 and self.attributes["jail_status"]):
            self.change_attributes("jail_status", False)

    def change_attributes(self, attribute, value):
        if attribute in self.attributes.keys():
            self.attributes[attribute] = value
            return True
        else: return False

    def get_answer(self, question):
        return random.randrange(self.rolling_range)


    def processMessage(self, msg):
        if isinstance(msg, RollMsg):
            if self.uuid != msg.data:
                return EmptyMsg()
            else:
                return MovementMsg(self.uuid, self.act())

        elif isinstance(msg, QuestionMsg):
            if self.uuid != msg.data[0]:
                return EmptyMsg()
            else:
                answer = self.get_answer(msg.data[1])
                space_id = msg.data[2]
                return AnswerMsg(self.uuid, space_id, answer)
            

        elif isinstance(msg, AttributeUpdateMsg):
            
            msg_player_id = msg.data[0]
            msg_attribute = msg.data[1] 
            msg_value = msg.data[2]

            if self.uuid != msg_player_id:
                return EmptyMsg()
            else:
                if msg_attribute != "coins":
                    self.change_attributes(msg_attribute, msg_value)
                    return NextTurnMsg()
                else:
                    self.attributes["coins"] += 1
                    if self.attributes["coins"] >= self.winning_count:
                        return GameOverMsg() 
                    else:
                        return AttributeUpdateMsg(self.uuid, "jail_status", False)
        else:
            return EmptyMsg()
