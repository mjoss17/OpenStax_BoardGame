import sys
sys.path.append("..")

from GameObjects.Player import Player
from GameObjects.Board import Board
from GameObjects.TurnDecider import TurnDecider
from GameObjects.Gamemaster import GameMaster
from Message.MovementMsg import MovementMsg
from Message.EmptyMsg import EmptyMsg
from Message.NextTurnMsg import NextTurnMsg
from Message.NewPlayerMsg import NewPlayerMsg
from Message.AnswerMsg import AnswerMsg
from Message.QuestionMsg import QuestionMsg
from Message.AttributeUpdateMsg import AttributeUpdateMsg
from Message.ErrorMsg import ErrorMsg
from Message.RollMsg import RollMsg

"""
message_tests.py

These tests make sure that messages passed between GameObjects
are being processed by the corect objects and ingored by the others
"""


def test_MovementMsg_ignore():

    newPlayer = Player("Tom")
    mvmtMsg = MovementMsg(newPlayer.uuid, 10)
    returnMsg = newPlayer.processMessage(mvmtMsg)
    assert(isinstance(returnMsg, type(EmptyMsg())))
    newTurnDecider = TurnDecider()
    returnMsg = newTurnDecider.processMessage(mvmtMsg)
    assert(isinstance(returnMsg, EmptyMsg))

def test_MovementMsg_accept():

    newPlayer = Player("Phil")
    mvmtMsg = MovementMsg(newPlayer.uuid, 10)
    newBoard = Board()
    playerMsg = NewPlayerMsg(newPlayer)
    assert(newBoard.num_players == 0)
    returnMsg = newBoard.processMessage(playerMsg)
    assert(newBoard.players2spaces[newPlayer.uuid] == 0)
    
    returnMsg = newBoard.processMessage(mvmtMsg)
    assert(isinstance(returnMsg, QuestionMsg))
    assert(newBoard.num_players == 1)
    assert(newBoard.players2spaces[newPlayer.uuid] == 10)

def test_AttributeUpdateMsg_accept():
    newPlayer = Player("Greg")
    assert(newPlayer.attributes["coins"] == 0)
    AUpdateMsg = AttributeUpdateMsg(newPlayer.uuid, "coins", 2)
    returnMsg = newPlayer.processMessage(AUpdateMsg)
    assert(isinstance(returnMsg, AttributeUpdateMsg))
    assert(newPlayer.attributes["coins"] == 2)

def test_AttributeUpdateMsg_ignore():
    newPlayer = Player("James")
    newBoard = Board(10)
    newTurnDecider = TurnDecider()
    AUpdateMsg = AttributeUpdateMsg(newPlayer.uuid, "coins", 2)
    returnMsg = newBoard.processMessage(AUpdateMsg)
    assert(isinstance(returnMsg, EmptyMsg))
    assert(newBoard.num_players == 0)
    returnMsg = newTurnDecider.processMessage(AUpdateMsg)
    assert(isinstance(returnMsg, EmptyMsg))

def test_NewPlayerMsg_accept():

    newPlayer = Player("Lucas")
    newBoard = Board(11)
    assert(newBoard.num_players == 0)
    playerMsg = NewPlayerMsg(newPlayer)
    returnMsg = newBoard.processMessage(playerMsg)
    assert(isinstance(returnMsg, NextTurnMsg))
    assert(newBoard.num_players == 1)

def test_NewPlayerMsg_ignore():
    newPlayer = Player("Christian")
    newTurnDecider = TurnDecider()
    playerMsg = NewPlayerMsg(newPlayer)
    returnMsg = newPlayer.processMessage(playerMsg)
    assert(isinstance(returnMsg, EmptyMsg))
    returnMsg = newTurnDecider.processMessage(playerMsg)
    assert(isinstance(returnMsg, EmptyMsg))

def test_faulty_AttributeUpdateMsg():
    newPlayer = Player("Chester")
    newBoard = Board(100)
    playerMsg = NewPlayerMsg(newPlayer)

    returnMsg =  newBoard.processMessage(playerMsg)
    assert(isinstance(returnMsg, NextTurnMsg))

    AUpdateMsg = AttributeUpdateMsg(newPlayer.uuid, "jail_status", True)
    returnMsg = newPlayer.processMessage(AUpdateMsg)
    assert(isinstance(returnMsg, NextTurnMsg))


    AUpdateMsg = AttributeUpdateMsg(newPlayer.uuid, "jail_status", False)
    returnMsg = newPlayer.processMessage(AUpdateMsg)
    assert(isinstance(returnMsg, NextTurnMsg))

    otherPlayer = Player("Lester")
    AUpdateMsg = AttributeUpdateMsg(otherPlayer.uuid, "jail_status", True)
    returnMsg = newPlayer.processMessage(AUpdateMsg)
    assert(isinstance(returnMsg, EmptyMsg))



    

if __name__ == "__main__":

    test_MovementMsg_ignore()
    test_MovementMsg_accept()
    test_AttributeUpdateMsg_accept()
    test_AttributeUpdateMsg_ignore()
    test_NewPlayerMsg_accept()
    test_NewPlayerMsg_ignore()
    test_faulty_AttributeUpdateMsg()
    print("Everything Passed")