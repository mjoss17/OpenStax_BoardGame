from GameObjects.GameObjectInterface import GameObjectInterface
from GameObjects.Space import Space
from Message.EmptyMsg import EmptyMsg
from Message.MovementMsg import MovementMsg
from Message.NewPlayerMsg import NewPlayerMsg
from Message.ErrorMsg import ErrorMsg
from Message.NextTurnMsg import NextTurnMsg

class Board(GameObjectInterface):

    spaces = []
    numSpaces = 12
    players = []
    players2spaces = {}

    def __init__(self, num_spaces = 12):
        if (type(num_spaces) is int and num_spaces > 0 and num_spaces < 1000):
            self.numSpaces = num_spaces

        for i in range(self.numSpaces):
            self.spaces.append(Space(i, self.getCategory(i)))


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
                    newSpace = self.players2spaces[player_id] + distance
                    # Right now the Board is circular, has no end
                    self.players2spaces[player_id] = newSpace % self.numSpaces
                    return NextTurnMsg()

            if len(self.players) == 0:
                return ErrorMsg("MovementMsg was sent to a board with no players")
            else:
                return ErrorMsg("MovementMsg was sent with invalid player")

        else:
            return EmptyMsg()



        

        