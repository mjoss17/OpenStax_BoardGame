import sys
import sys
sys.path.append("..")

from GameObjects.Player import Player
from GameObjects.Gamemaster import GameMaster
from Message.PurseUpdateMsg import PurseUpdateMsg
from Message.MovementMsg import MovementMsg
from Message.EmptyMsg import EmptyMsg
from Message.NextTurnMsg import NextTurnMsg


def test_MovementMsg():

    newPlayer = Player("Tom")

    mvmtMsg = MovementMsg(10)
    returnMsg = newPlayer.processMessage(mvmtMsg)
    assert(isinstance(returnMsg, type(EmptyMsg())))

    PurseMsg = PurseUpdateMsg(10)
    returnMsg = newPlayer.processMessage(PurseMsg)
    assert(isinstance(returnMsg, type(NextTurnMsg())))



if __name__ == "__main__":

    test_MovementMsg()
    print("Everything passed")