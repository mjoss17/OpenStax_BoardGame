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
from Message.RollMsg import RollMsg

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

def test_CoinsUpdateMsg():
    newPlayer = Player("Greg")
    PurseMsg = AttributeUpdateMsg(newPlayer.uuid, "coins", 10)
    returnMsg = newPlayer.processMessage(PurseMsg)
    assert(isinstance(returnMsg, AttributeUpdateMsg))
    assert(newPlayer.attributes["coins"] == 10)
    assert(newPlayer.attributes["jail_status"] == False)

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
    nextPlayer = Player("Timmy")
    newBoard = Board(5)

    playerMsg = NewPlayerMsg(nextPlayer)
    returnMsg = newBoard.processMessage(playerMsg)
    print(newBoard.num_players())
    assert(newBoard.num_players() == 1)
    
    mvmtMsg = MovementMsg(nextPlayer.uuid, 1)
    returnMsg = newBoard.processMessage(mvmtMsg)
    assert(isinstance(returnMsg, QuestionMsg))
    
    returnMsg = nextPlayer.processMessage(returnMsg)
    assert(isinstance(returnMsg, AnswerMsg))

    returnMsg = newBoard.processMessage(returnMsg)
    assert(isinstance(returnMsg, AttributeUpdateMsg))

    returnMsg = nextPlayer.processMessage(returnMsg)
    assert(isinstance(returnMsg, AttributeUpdateMsg))
    assert(nextPlayer.attributes["coins"] == 1)
    assert(nextPlayer.attributes["jail_status"] == False)

    returnMsg = nextPlayer.processMessage(returnMsg)
    assert(nextPlayer.attributes["jail_status"] == False)

def test_JailStatus_change():
    newPlayer = Player("Jose")
    newBoard = Board(5)

    playerMsg = NewPlayerMsg(newPlayer)
    returnMsg = newBoard.processMessage(playerMsg)

    rollMsg = RollMsg(newPlayer.uuid)


    

if __name__ == "__main__":

    test_MovementMsg()
    test_CoinsUpdateMsg()
    test_AttributeUpdateMsg()
    test_QuestionMsg()
    print("Everything Passed")