import sys
sys.path.append("..")

from GameObjects.Player import Player
from GameObjects.Gamemaster import GameMaster
from GameObjects.Board import Board
from GameObjects.Purse import Purse

def test_Player_creation():
    newPlayer = Player("Greg")
    assert (newPlayer.act() > 0)
    assert (newPlayer.name == "Greg")

    newPlayer = Player(32)
    assert(newPlayer.name == "32")

    assert(newPlayer.purse.add(1) == 1)
    assert(newPlayer.purse.add(-1) == 0)
    assert(newPlayer.purse.add(2) == 2)


def test_Gamemaster_creation():
    newGamemaster = GameMaster()
    assert (newGamemaster.act() == "Nothing to do")

def test_Board_creation():
    newBoard = Board(-5)
    assert (newBoard.numSpaces == 12)
    newBoard = Board()
    assert (newBoard.numSpaces == 12)
    newBoard = Board(100000)
    assert (newBoard.numSpaces == 12)
    newBoard = Board(11)
    assert (newBoard.numSpaces == 11)


if __name__ == "__main__":
    test_Player_creation()
    test_Gamemaster_creation()
    test_Board_creation()
    print("Everything passed")