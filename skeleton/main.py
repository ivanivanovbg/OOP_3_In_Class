from datetime import date, timedelta
from board import Board
from board_item import BoardItem
from event_log import EventLog
from task import Task
from issue import Issue

def add_days_to_now(d):
    return date.today() + timedelta(days=d)


item = BoardItem('Refactor this mess', add_days_to_now(2))
anotherItem = BoardItem('Dont refactor anything',  add_days_to_now(2))

board = Board()
board.add_item(item)
board.add_item(anotherItem)

task = Task('Test the application flow', 'Steven', add_days_to_now(2))
task.advance_status()
task.advance_status()
task.assignee = 'Not Steven'
print(task.history())

issue = Issue('App flow tests?', 'We need to test the flow!', add_days_to_now(1))
issue.advance_status()
issue.due_date += timedelta(days = 1)
print(issue.history())

issue = Issue('App flow tests?', 'We need to test the flow!', add_days_to_now(1))
task = Task('Dont refactor anything', 'Pesho', add_days_to_now(2))

print(issue.info())
print(task.info())