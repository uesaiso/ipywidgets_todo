from ipywidgets import Button, Checkbox, HBox

from ..store import Todo, TodoStore, todo_store


class TodoItem(HBox):
    def __init__(
        self, todo: Todo, index: int, store: TodoStore = todo_store, *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.store = store
        self.index = index
        self.checkbox = Checkbox(value=todo.completed, description=todo.text)
        self.delete_button = Button(description="Delete")

        self.checkbox.observe(self.toggle_todo, names="value")
        self.delete_button.on_click(self.delete_todo)

        self.children = [self.checkbox, self.delete_button]

    def toggle_todo(self, change: dict) -> None:
        self.store.toggle_todo(self.index)

    def delete_todo(self, button: Button) -> None:
        self.store.remove_todo(self.index)
