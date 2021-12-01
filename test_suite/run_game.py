import sys
sys.path.append("..")

from Game import GameUpdated


def test_Game_creation():
    game = GameUpdated(12)
    game.add_player("Matt")
    game.add_player("Ripal")

    game.start()


if __name__ == "__main__":

    test_Game_creation()
    print("Everything Passed")