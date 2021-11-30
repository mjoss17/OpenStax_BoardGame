import sys
sys.path.append("..")

from Game import Game_Update


def test_Game_creation():
    game = Game_Update(5)
    game.add_player("Matt")
    game.add_player("Ripal")

    game.start()


if __name__ == "__main__":




    print("Everything Passed")