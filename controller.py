"""
class TodoController

Connects GUI events (user input) to updates in the TodoModel and TodoView

In general, each button in a GUI will have a corresponding method in a controller

Buttons have "clicked" events in PySide6 (and most GUI frameworks), which can be
"connected" to methods. These methods are sometimes called "handler methods."
For example, the view may have an "add" button, "view.add_button". With no
connections, clicking this button would do nothing. But, by connecting a method
to this button's "clicked" event, we can trigger an action whenever the button is
clicked.

For optimal separation of concerns, these "handler" methods are encapsulated into
a "Controller" class, which also handles the making of the connections with a 
"setup_connections()" method that gets called right away when the Controller class 
is initialized.

The syntax and organization looks like this:

- View has a button called "add_button" that is supposed to add something to something else
- Controller has a method ("handler method") called "add_task"
    "add_task" is where the logic goes for adding whatever needs to be added
- Controller gets initialized with a model and view
- By writing (inside the Controller class, upon initialization)
    self.view.add_button.clicked.connect(self.add_task),
    we tell the program that "when the view's button called add_button gets clicked, 
    call the method self.add_task
"""
# controller.py

from model import TodoModel
from view import TodoView

class TodoController:
    def __init__(self, model: TodoModel, view: TodoView):
        self.model = model
        self.view = view

        self.setup_connections()

    def setup_connections(self):
        # Connect "clicked" events to controller methods (callbacks)
        self.view.add_button.clicked.connect(self.add_task)
        self.view.remove_button.clicked.connect(self.remove_task)
        self.view.clear_button.clicked.connect(self.clear_tasks)

    def add_task(self):
        """
        Adds a new task to the model and updates the view

        When the "Add Task" button is clicked by the user, this method
        gets called. 
        
        - First, the task text is extracted from the view
            using the TodoView.get_task_input() method.
        
        - Second, the task text is added to the model using the
            TodoModel.add_task() method.
        
        - Third, the new task text is added to view's task list
            using the TodoView.add_task_to_list() method
        
        - Fourth, the input field for the view is cleared, to let
            the user know that they can type a new task, using the
            TodoView.clear_task_input() method.
        """
        task_text = self.view.get_task_input()
        if task_text:
            task_index = self.model.add_task(task_text)
            self.view.add_task_to_list(task_text)
            self.view.clear_task_input()

    def remove_task(self):
        task_index = self.view.get_selected_task_index()
        if task_index is not None:
            self.model.remove_task(task_index)
            self.view.remove_selected_task()

    def clear_tasks(self):
        self.model.clear_tasks()
        self.view.clear_task_list()
