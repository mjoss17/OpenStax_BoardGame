from GameObjects.Player import Player
from GameObjects.Board import Board
from GameObjects.TurnDecider import TurnDecider
from Message.EmptyMsg import EmptyMsg
from Message.ErrorMsg import ErrorMsg
from Message.GameOverMsg import GameOverMsg
from Message.NewPlayerMsg import NewPlayerMsg
from Message.NextTurnMsg import NextTurnMsg
from Message.RollMsg import RollMsg

class Game_Update:

    game_objects = []

    def __init__(self, num_spaces):

        board = Board(num_spaces)
        self.game_objects.append(board)

        for s in board.getSpaces():
            self.game_objects.append(s)

        self.turnDecider = TurnDecider()
        self.game_objects.append(self.turnDecider)

    def add_player(self, name):
        newPlayer = Player(name)
        self.game_objects.append(newPlayer)

        playerMsg = NewPlayerMsg(newPlayer)
        self.send_message(playerMsg)

    def send_message(self, msg):
        response_queue = []
        for obj in self.game_objects:
            response_queue.append(obj.processMessage(msg))
        
        return response_queue


    def start(self):
        while(True):
            player_id = self.turnDecider.get_next_up()
            rollMsg = RollMsg(player_id)
            response_queue = self.send_message(rollMsg)

            nextMove = False
            gameOver = False
            while len(response_queue) != 0:
                resp = response_queue.pop(0)
                if isinstance(resp, NextTurnMsg):
                    nextMove = True
                elif isinstance(resp, ErrorMsg):
                    print("Error: Stopping")
                    exit()
                elif isinstance(resp, GameOverMsg):
                    gameOver = True
                elif isinstance(resp, EmptyMsg):
                    continue
                elif resp == None:
                    continue
                else:
                    response_queue.extend(self.send_message(resp))

            if not nextMove:
                print("Error: No next move Confirmation was received")
                exit()
            if gameOver:
                break
        
        print("Game Over")
                    
            
            






