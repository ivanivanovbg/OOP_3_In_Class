from skeleton.board_item import BoardItem
from datetime import date
from item_status import ItemStatus

class Task(BoardItem):
    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self,value):
        if 5 <= len(value) <= 30:
            if hasattr(self,'_assignee'):
                super()._log_event(f"Assignee changed from {self._assignee} to {value}")
            self._assignee = value
        else:
            raise ValueError("Assignee length must be [5,30]")


    def __init__(self,title:str,assignee:str,due_date:date):
        super().__init__(title,due_date)
        self.assignee = assignee
        self._status = ItemStatus.TODO


    def info(self):
        if hasattr(self,'_assignee'):
            return f"Task (assigned to :{self._assignee}) "+super().info()
        else:
            return super().info()