import sys
sys.path.append("..")
from Player import Player
from ParticipantInterface import ParticipantInterface
from Gamemaster import GameMaster

newPlayer = Player("greg")
print(newPlayer.act())