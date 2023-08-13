from ipywidgets import Text, VBox

from ..store import TodoStore, todo_store
from .todo_item import TodoItem


class TodoList(VBox):
    """A widget that displays a list of Todo items."""

    def __init__(self, store: TodoStore = todo_store, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.store = store
        self.new_todo_input = Text(placeholder="New Todo")
        self.new_todo_input.on_submit(self.add_todo)
        self.children = [self.new_todo_input]

        self.store.observe(self.update_todos, names="todos")
        self.update_todos()

    def add_todo(self, change: dict = None) -> None:
        """Adds a new Todo item using the text from the text widget."""
        self.store.add_todo(self.new_todo_input.value)
        self.new_todo_input.value = ""

    def update_todos(self, change: dict = None) -> None:
        """Updates the Todo list based on the current state of the store."""
        self.children = [self.new_todo_input] + [
            TodoItem(todo, index=idx) for idx, todo in enumerate(self.store.todos)
        ]
