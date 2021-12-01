
from Message.MessageInterface import MessageInterface

"""
EmptyMsg
Sent by any GameObject to acknolege, but not do anything with a Message
"""
class EmptyMsg(MessageInterface):
    pass