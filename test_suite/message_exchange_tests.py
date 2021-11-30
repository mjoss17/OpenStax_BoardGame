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

def test_QuestionAndAnswerExchange():
    nextPlayer = Player("Timmy")
    newBoard = Board(5)

    playerMsg = NewPlayerMsg(nextPlayer)
    returnMsg = newBoard.processMessage(playerMsg)
    assert(newBoard.num_players == 1)
    
    mvmtMsg = MovementMsg(nextPlayer.uuid, 1)
    returnMsg = newBoard.processMessage(mvmtMsg)
    assert(isinstance(returnMsg, QuestionMsg))
    
    returnMsg = nextPlayer.processMessage(returnMsg)
    assert(isinstance(returnMsg, AnswerMsg))

    returnMsg = newBoard.processMessage(returnMsg)
    assert(isinstance(returnMsg, AttributeUpdateMsg))

    assert(nextPlayer.attributes["coins"] == 0)
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
    assert(isinstance(returnMsg, NextTurnMsg))

    rollMsg = RollMsg(newPlayer.uuid)
    mvmtMsg = newPlayer.processMessage(rollMsg)
    assert(isinstance(mvmtMsg, MovementMsg))

    jailedMsg = AttributeUpdateMsg(newPlayer.uuid, "jail_status", True)
    returnMsg = newPlayer.processMessage(jailedMsg)
    assert(newPlayer.attributes["jail_status"] == True)

    returnMsg = newBoard.processMessage(mvmtMsg)
    assert(isinstance(returnMsg, QuestionMsg))
    
    returnMsg = newPlayer.processMessage(returnMsg)
    assert(isinstance(returnMsg, AnswerMsg))

    returnMsg = newBoard.processMessage(returnMsg)
    assert(isinstance(returnMsg, AttributeUpdateMsg))

    assert(newPlayer.attributes["coins"] == 0)
    returnMsg = newPlayer.processMessage(returnMsg)
    assert(isinstance(returnMsg, AttributeUpdateMsg))
    assert(newPlayer.attributes["coins"] == 1)
    assert(newPlayer.attributes["jail_status"] == True)

    returnMsg = newPlayer.processMessage(returnMsg)
    assert(newPlayer.attributes["jail_status"] == False)


if __name__ == "__main__":

    test_QuestionAndAnswerExchange()
    test_JailStatus_change()
    print("Everything Passed")