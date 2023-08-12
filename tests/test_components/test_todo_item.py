import pytest
import pytest_mock
from jupyter_sandbox.components.todo_item import TodoItem
from jupyter_sandbox.store.todo_store import TodoStore


@pytest.fixture
def todo_item(todo_store: TodoStore) -> TodoItem:
    todo = todo_store.todos[0]
    return TodoItem(todo, index=0, store=todo_store)


def test_toggle_todo(
    todo_item: TodoItem, todo_store: TodoStore, mocker: pytest_mock.MockFixture
) -> None:
    todo_item.checkbox.value = True
    assert todo_store.todos[0].completed is True
    todo_item.checkbox.value = False
    assert todo_store.todos[0].completed is False


def test_delete_todo(todo_item: TodoItem, todo_store: TodoStore) -> None:
    todo_item.delete_todo(todo_item.delete_button)
    assert len(todo_store.todos) == 0
