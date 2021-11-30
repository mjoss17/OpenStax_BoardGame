import sys
sys.path.append("..")
from Player import Player
from ParticipantInterface import ParticipantInterface
from Gamemaster import GameMaster

def test_Player_creation():

    newPlayer = Player("Greg")
    assert (newPlayer.act() > 0)
    assert (newPlayer.name == "Greg")

    assert(newPlayer.purse.exchange(1) == 1)
    assert(newPlayer.purse.exchange(-1) == 0)
    assert(newPlayer.purse.exchange(2) == 2)

def test_Gamemaster_creation():

    newGamemaster = GameMaster()
    assert (newGamemaster.act() == "Nothing to do")

if __name__ == "__main__":
    test_Player_creation()
    test_Gamemaster_creation()
    print("Everything passed")