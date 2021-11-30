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
from Message.AnswerMsg import AnswerMsg
from Message.QuestionMsg import QuestionMsg
from Message.AttributeUpdateMsg import AttributeUpdateMsg
from Message.ErrorMsg import ErrorMsg


def test_MovementMsg():

    newPlayer = Player("Tom")
    mvmtMsg = MovementMsg(newPlayer.uuid, 10)
    returnMsg = newPlayer.processMessage(mvmtMsg)
    assert(isinstance(returnMsg, type(EmptyMsg())))

    newBoard = Board()
    playerMsg = NewPlayerMsg(newPlayer)
    returnMsg = newBoard.processMessage(playerMsg)
    returnMsg = newBoard.processMessage(mvmtMsg)
    assert(isinstance(returnMsg, QuestionMsg))

def test_PurseUpdateMsg():
    newPlayer = Player("Greg")
    PurseMsg = PurseUpdateMsg(newPlayer.uuid, 10)
    returnMsg = newPlayer.processMessage(PurseMsg)
    assert(isinstance(returnMsg, type(NextTurnMsg())))

    newBoard = Board(11)
    playerMsg = NewPlayerMsg(newPlayer)
    returnMsg = newBoard.processMessage(playerMsg)
    assert(isinstance(returnMsg, type(NextTurnMsg())))

def test_AttributeUpdateMsg():
    newPlayer = Player("Chester")
    newBoard = Board(100)
    playerMsg = NewPlayerMsg(newPlayer)

    returnMsg =  newBoard.processMessage(playerMsg)
    assert(isinstance(returnMsg, type(NextTurnMsg())))

    AUpdateMsg = AttributeUpdateMsg(newPlayer.uuid, "jail_status", True)
    returnMsg = newPlayer.processMessage(AUpdateMsg)
    assert(isinstance(returnMsg, NextTurnMsg))

    AUpdateMsg = AttributeUpdateMsg(newPlayer.uuid, "height", 72)
    returnMsg = newPlayer.processMessage(AUpdateMsg)
    assert(isinstance(returnMsg, ErrorMsg))

    AUpdateMsg = AttributeUpdateMsg(newPlayer.uuid, "jail_status", False)
    returnMsg = newPlayer.processMessage(AUpdateMsg)
    assert(isinstance(returnMsg, NextTurnMsg))

    otherPlayer = Player("Lester")
    AUpdateMsg = AttributeUpdateMsg(otherPlayer.uuid, "jail_status", True)
    returnMsg = newPlayer.processMessage(AUpdateMsg)
    assert(isinstance(returnMsg, EmptyMsg))


def test_QuestionMsg():
    newPlayer = Player("Timmy")
    newBoard = Board(5)

    playerMsg = NewPlayerMsg(newPlayer)
    returnMsg = newBoard.processMessage(playerMsg)
    
    mvmtMsg = MovementMsg(newPlayer.uuid, 1)
    returnMsg = newBoard.processMessage(mvmtMsg)
    assert(isinstance(returnMsg, QuestionMsg))
    
    returnMsg = newPlayer.processMessage(returnMsg)
    assert(isinstance(returnMsg, AnswerMsg))

    returnMsg = newBoard.processMessage(returnMsg)
    assert(isinstance(returnMsg, PurseUpdateMsg))

if __name__ == "__main__":

    test_MovementMsg()
    test_PurseUpdateMsg()
    test_AttributeUpdateMsg()
    print("Everything Passed")