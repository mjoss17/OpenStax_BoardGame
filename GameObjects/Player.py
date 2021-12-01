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

'''
Player - implements GameObjectInterface, implements ParticipantInterface
Contains:
name, uuid, attributes{}

Handles:
QuestionMsg, RollMsg, and AttributeUpdateMsg

Emits:
NextTurnMsg, EmptyMsg, ErrorMsg, AttributeMsg, MovementMsg, GameoverMsg, AnswerMsg
'''
class Player(ParticipantInterface):
    
    rolling_range = 6
    winning_count = 10

    def __init__(self, name):
        self.name = str(name)
        self.uuid = uuid.uuid4()
        self.attributes = {"jail_status" : False, "coins" : 0}

    def name(self):
        return self.name

    def act(self):
        roll = random.randrange(self.rolling_range + 1)
        self.rolled_message(roll)
        return self.check_attribute_updates(roll)

    def check_attribute_updates(self, new_roll):
        if (self.attributes["jail_status"]):
            if (new_roll % 2 == 0):
                self.change_attributes("jail_status", False)
                return new_roll 
            else:
                return None
        return new_roll

    def change_attributes(self, attribute, value):
        if attribute in self.attributes.keys():
            self.attributes[attribute] = value
            return True
        else: return False

    def get_answer(self, question):
        return random.randrange(self.rolling_range)

    def winning_message(self):
        print("%s WINS!!! with %d points!" % (self.name, self.attributes["coins"]))

    def scored_message(self):
        print("%s scored, now has %d coins" % (self.name, self.attributes["coins"]))

    def rolled_message(self, num):
        print("%s rolled a %d" % (self.name, num))

    def describe_question(self, q):
        print("Question is: %s" % q)
    
    def describe_answer(self, answer):
        print("Answer: %s" % answer)

    def describe_jail(self):
        print("Jail status %s: %s" % (self.name, self.attributes["jail_status"]))

    def describe_still_jailed(self):
        print("%s still in Jail" % self.name)

    def processMessage(self, msg):
        # Hande RollMsg
        if isinstance(msg, RollMsg):
            if self.uuid != msg.data:
                return EmptyMsg()
            else:
                roll = self.act()
                if roll == None:
                    self.describe_still_jailed()
                    return NextTurnMsg()
                else:
                    return MovementMsg(self.uuid, roll)

        # Handle QuestionMsg
        elif isinstance(msg, QuestionMsg):
            if self.uuid != msg.data[0]:
                return EmptyMsg()
            else:
                # self.describe_question(msg.data[1])
                answer = self.get_answer(msg.data[1]) ### here
                self.describe_answer(answer)
                space_id = msg.data[2]
                return AnswerMsg(self.uuid, space_id, answer)
            
        # Handle AttributeUpdateMsg
        elif isinstance(msg, AttributeUpdateMsg):
            
            msg_player_id = msg.data[0]
            msg_attribute = msg.data[1] 
            msg_value = msg.data[2]

            if self.uuid != msg_player_id:
                return EmptyMsg()
            else:
                if msg_attribute != "coins":
                    self.change_attributes(msg_attribute, msg_value)
                    self.describe_jail()
                    return NextTurnMsg()
                else:
                    self.attributes["coins"] += msg_value
                    self.scored_message()
                    if self.attributes["coins"] >= self.winning_count:
                        self.winning_message()
                        return GameOverMsg() 
                    else:
                        return AttributeUpdateMsg(self.uuid, "jail_status", False)
        else:
            return EmptyMsg()
