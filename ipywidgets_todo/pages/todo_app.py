from ipywidgets import VBox

from ..components import TodoList


class TodoApp(VBox):
    """A widget that displays the entire Todo app."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.children = [TodoList()]
