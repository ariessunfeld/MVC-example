"""
class TodoView

Contains the GUI elements

Has methods to get text from various fields in the GUI, and clear text from various fields
"""
# view.py

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget

class TodoView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To-Do List")

        self.layout = QVBoxLayout()

        # Add the text entry box for new Todo items
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a new task")
        self.layout.addWidget(self.task_input)

        # Add the "Add Task" button
        self.add_button = QPushButton("Add Task", self)
        self.layout.addWidget(self.add_button)

        # Add a list to display tasks
        self.task_list = QListWidget(self)
        self.layout.addWidget(self.task_list)

        # Add a button to remove selected tasks
        self.remove_button = QPushButton("Remove Selected Task", self)
        self.layout.addWidget(self.remove_button)

        # Add a button to clear all tasks
        self.clear_button = QPushButton("Clear All Tasks", self)
        self.layout.addWidget(self.clear_button)

        # Set the layout for this widget
        self.setLayout(self.layout)

    def get_task_input(self):
        return self.task_input.text()

    def clear_task_input(self):
        self.task_input.clear()

    def add_task_to_list(self, task):
        self.task_list.addItem(task)

    def remove_selected_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            self.task_list.takeItem(self.task_list.row(item))

    def clear_task_list(self):
        self.task_list.clear()

    def get_selected_task_index(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            return None
        return self.task_list.row(selected_items[0])
