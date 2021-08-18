from enum import Enum

class ActionType(str, Enum):
    do_not_sell = "org.consumer.do_not_sell"
    delete      = "org.consumer.delete"
    access      = "org.consumer.access"

class ActionState(str, Enum):
    pending = "pending"
    closed  = "closed"
    opened  = "open"

    def is_open(self):
        return (self in ["pending", "open"])

    def is_closed(self):
        return not self.is_open()
