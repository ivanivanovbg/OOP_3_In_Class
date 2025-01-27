from skeleton.board_item import BoardItem
from datetime import date

class Issue(BoardItem):
    @property
    def description(self):
        return self._description

    def __init__(self,title:str,description:str,due_date:date):
        super().__init__(title,due_date)
        if description != "":
            self._description = description
        else:
            self._description = "No description"

    def info(self):
        if hasattr(self,"_description"):
            return f"Issue ({self._description}) "+super().info()
        else:
            return super().info()