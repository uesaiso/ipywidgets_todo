from ipywidgets import Text, VBox

from ..store import TodoStore, todo_store
from .todo_item import TodoItem


class TodoList(VBox):
    def __init__(self, store: TodoStore = todo_store, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.store = store
        self.new_todo_input = Text(placeholder="New Todo")
        self.new_todo_input.on_submit(self.add_todo)
        self.children = [self.new_todo_input]

        self.store.observe(self.update_todos, names="todos")
        self.update_todos()

    def add_todo(self, text_widget: Text) -> None:
        self.store.add_todo(text_widget.value)
        self.new_todo_input.value = ""

    def update_todos(self, change: dict = None) -> None:
        self.children = [self.new_todo_input] + [
            TodoItem(todo, index=idx) for idx, todo in enumerate(self.store.todos)
        ]
