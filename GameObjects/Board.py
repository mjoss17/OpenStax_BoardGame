from GameObjects.GameObjectInterface import GameObjectInterface
from GameObjects.Space import Space
from Message.AnswerMsg import AnswerMsg
from Message.EmptyMsg import EmptyMsg
from Message.MovementMsg import MovementMsg
from Message.NewPlayerMsg import NewPlayerMsg
from Message.ErrorMsg import ErrorMsg
from Message.NextTurnMsg import NextTurnMsg
from Message.QuestionMsg import QuestionMsg
from Message.AttributeUpdateMsg import AttributeUpdateMsg


'''
Board - implements GameObjectInterface
Contains:
Players[], Spaces[], players2spaces{}

Handles:
NewPlayerMsg, MovementMsg, and AnswerMsg

Emits:
NextTurnMsg, EmptyMsg, QuestionMsg, ErrorMsg and AttributeUpdateMsg
'''
class Board(GameObjectInterface):

    max_boardsize = 1000
    min_boardsize = 1
    default_boardsize = 12

    def __init__(self, num_spaces = default_boardsize, answer = 0):
        self.players = []
        self.spaces = []
        self.players2spaces = {}
        if (type(num_spaces) is int and num_spaces > self.min_boardsize and num_spaces < self.max_boardsize):
            self.num_spaces = num_spaces
        else: 
            self.num_spaces = self.default_boardsize

        for i in range(self.num_spaces):
            self.spaces.append(Space(i, self.getCategory(i)))

    def get_spaces(self):
        return self.spaces
    
    @property
    def num_players(self):
        return len(self.players)

    def getCategory(self, i):
        if i%12 == 0: return 'Pop'
        if i%12 == 4: return 'Pop'
        if i%12 == 8: return 'Pop'
        if i%12 == 1: return 'Science'
        if i%12 == 5: return 'Science'
        if i%12 == 9: return 'Science'
        if i%12 == 2: return 'Sports'
        if i%12 == 6: return 'Sports'
        if i%12 == 10: return 'Sports'
        else: return 'Rock'

    def describe_move(self, position):
        print("Is now on space %d" %position)

    def describe_category(self, new_space):
        print("Category is: %s" % self.spaces[new_space].category)

    def processMessage(self, msg):

        if isinstance(msg, NewPlayerMsg):
            player = msg.data
            self.players.append(player)
            self.players2spaces[player.uuid] = 0
            print("Board has a New Player - %s" % msg.data.name)
            return NextTurnMsg()
            
        elif isinstance(msg, MovementMsg):
            player_id = msg.data[0]
            distance = msg.data[1]
            for p in self.players:
                if p.uuid == player_id:
                    new_space = (self.players2spaces[player_id] + distance) % self.num_spaces
                    self.describe_move(new_space)
                    self.players2spaces[player_id] = new_space
                    self.describe_category(new_space)
                    question = self.spaces[new_space].get_question()
                    return QuestionMsg(player_id, question, new_space)

            if len(self.players) == 0:
                return ErrorMsg("MovementMsg was sent to a board with no players")
            else:
                return ErrorMsg("MovementMsg was sent with invalid player")

        elif isinstance(msg, AnswerMsg):
            sender = msg.data[0]
            space = self.spaces[msg.data[1]]
            answer = msg.data[2]
            if space.check_answer(answer):
                return AttributeUpdateMsg(sender, "coins", 1)
            else:
                return AttributeUpdateMsg(sender, "jail_status", True)


        else:
            return EmptyMsg()



        

        