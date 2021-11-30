import sys
import sys
sys.path.append("..")

from GameObjects.Player import Player
from GameObjects.Board import Board
from GameObjects.Gamemaster import GameMaster
from Message.PurseUpdateMsg import PurseUpdateMsg
from Message.MovementMsg import MovementMsg
from Message.EmptyMsg import EmptyMsg
from Message.NextTurnMsg import NextTurnMsg
from Message.NewPlayerMsg import NewPlayerMsg


def test_MovementMsg():

    newPlayer = Player("Tom")
    mvmtMsg = MovementMsg(newPlayer.uuid, 10)
    returnMsg = newPlayer.processMessage(mvmtMsg)
    assert(isinstance(returnMsg, type(EmptyMsg())))

    newBoard = Board()
    playerMsg = NewPlayerMsg(newPlayer)
    returnMsg = newBoard.processMessage(playerMsg)
    returnMsg = newBoard.processMessage(mvmtMsg)
    assert(isinstance(returnMsg, type(NextTurnMsg())))

def test_PurseUpdateMsg():
    newPlayer = Player("Tom")
    PurseMsg = PurseUpdateMsg(10)
    returnMsg = newPlayer.processMessage(PurseMsg)
    assert(isinstance(returnMsg, type(NextTurnMsg())))




if __name__ == "__main__":

    test_MovementMsg()
    print("Everything passed")