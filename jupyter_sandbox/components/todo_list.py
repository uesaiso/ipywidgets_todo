from collections.abc import Callable

from ipywidgets import Text, VBox, Widget

from ..store import Todo, TodoStore, todo_store
from .todo_item import TodoItem


def create_todo_item(item: Todo, index: int) -> TodoItem:
    return TodoItem(todo=item, index=index)


class TodoList(VBox):
    def __init__(self, store: TodoStore = todo_store, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.store = store
        self.new_todo_input = Text(placeholder="New Todo")
        self.new_todo_input.on_submit(self.add_todo)

        self.store.observe(self.update_ui, names="todos")
        self.todo_list = [
            TodoItem(todo, index=idx) for idx, todo in enumerate(self.store.todos)
        ]
        self.children = [self.new_todo_input] + self.todo_list

    def add_todo(self, text_widget: Text) -> None:
        self.store.add_todo(text_widget.value)
        self.new_todo_input.value = ""

    def update_ui(self, change: dict) -> None:
        self.children = [self.new_todo_input] + self.diff_widgets_list(
            change, self.todo_list, create_todo_item
        )

    def diff_widgets_list(
        self,
        change: dict,
        widget_list: list[Widget],
        widget_factory: Callable[..., Widget],
    ) -> list[Widget]:
        if not isinstance(change["old"], list) and isinstance(change["new"], list):
            raise ValueError("changed value must be a list")
        new_list = widget_list.copy()
        old_items = change["old"]
        new_items = change["new"]

        # Identify items to be removed
        items_to_remove = [item for item in old_items if item not in new_items]
        for item in items_to_remove:
            idx = old_items.index(item)
            new_list.pop(idx)

        # Identify items to be added
        items_to_add = [item for item in new_items if item not in old_items]
        for item in items_to_add:
            idx = new_items.index(item)
            new_list.insert(idx, widget_factory(item, idx))
        return new_list
