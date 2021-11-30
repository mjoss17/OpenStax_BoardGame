from GameObjects.Player import Player
from GameObjects.Board import Board
from GameObjects.TurnDecider import TurnDecider
from Message.ErrorMsg import ErrorMsg
from Message.GameOverMsg import GameOverMsg
from Message.NewPlayerMsg import NewPlayerMsg
from Message.NextTurnMsg import NextTurnMsg

class Game_Update:

    game_objects = []

    def __init__(self, num_spaces):

        board = Board(num_spaces)
        self.game_objects.append(board)

        for s in board.getSpaces():
            self.game_objects.append(s)

        self.turnDecider = TurnDecider()

    def add_player(self, name):
        newPlayer = Player(name)
        self.game_objects.append(newPlayer)

        playerMsg = NewPlayerMsg(newPlayer)
        self.send_message(playerMsg)

    def send_message(self, msg):
        response_queue = []
        for obj in self.game_objects:
            response_queue.append(obj.processMessage(msg))
        
        nextMove = False
        gameOver = False
        for resp in response_queue:
            if isinstance(resp, NextTurnMsg):
                nextMove = True
            elif isinstance(resp, ErrorMsg):
                print("Error: Stopping")
                break
            elif isinstance(resp, GameOverMsg):
                gameOver = True
            else:
                pass

    # def start(self):
    #     while(True):
    #         player_id = self.turnDecider.get_next_up()
            






