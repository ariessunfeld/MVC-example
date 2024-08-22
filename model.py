"""
class TodoModel

Model represents the state of the Todo List
Model has methods for adding / removing tasks, as well as getting and clearing all tasks
"""
# model.py

class TodoModel:
    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        self._tasks.append(task)
        return len(self._tasks) - 1

    def remove_task(self, index):
        if 0 <= index < len(self._tasks):
            self._tasks.pop(index)

    def get_tasks(self):
        return self._tasks

    def clear_tasks(self):
        self._tasks.clear()
