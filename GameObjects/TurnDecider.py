from GameObjects.GameObjectInterface import GameObjectInterface
from GameObjects.Player import Player
from Message.EmptyMsg import EmptyMsg
from Message.NewPlayerMsg import NewPlayerMsg
from Message.NextTurnMsg import NextTurnMsg

class TurnDecider(GameObjectInterface):

    def __init__(self):
        self.player_order = []
        self.current_pos = 0

    @property
    def num_players(self):
        return len(self.player_order)

    def add_player(self, player):
        self.player_order.append(player.uuid)

    def get_next_up(self):
        if len(self.player_order) > 0:
            next_id = self.player_order[self.current_pos % self.num_players]
            self.current_pos += 1
            return next_id

    def processMessage(self, msg):
        # print("Turn Decider got %s " % msg.data)
        if isinstance(msg, NewPlayerMsg):
            self.add_player(msg.data)
            return EmptyMsg()
        else:
            return EmptyMsg()
