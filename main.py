
# main.py

import sys
from PySide6.QtWidgets import QApplication
from model import TodoModel
from view import TodoView
from controller import TodoController

def main():
    app = QApplication(sys.argv)

    model = TodoModel()                      # Instantiate the model
    view = TodoView()                        # Instantiate the view
    controller = TodoController(model, view) # Instantiate the controller

    # Note: Instantiating the controller sets up the connections between the 
    # model and view, allowing the buttons in the GUI to do something when clicked

    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
