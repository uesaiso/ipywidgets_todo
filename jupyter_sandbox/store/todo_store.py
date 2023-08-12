from dataclasses import dataclass

from traitlets import HasTraits, List


@dataclass(frozen=True)
class Todo:
    text: str
    completed: bool

    def __post_init__(self) -> None:
        if not len(self.text) > 0:
            raise ValueError("Todo text must be a non-empty string")


class TodoStore(HasTraits):
    todos = List([])

    def add_todo(self, text: str, completed: bool = False) -> None:
        self.todos = self.todos + [Todo(text=text, completed=completed)]

    def toggle_todo(self, index: int) -> None:
        old_todo = self.todos[index]
        new_todo = Todo(old_todo.text, not old_todo.completed)
        self.todos = [
            new_todo if idx == index else todo for idx, todo in enumerate(self.todos)
        ]

    def remove_todo(self, index: int) -> None:
        self.todos = [todo for idx, todo in enumerate(self.todos) if idx != index]


todo_store = TodoStore()
