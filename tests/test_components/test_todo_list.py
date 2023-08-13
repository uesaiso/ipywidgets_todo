import pytest
from ipywidgets_todo.components.todo_list import TodoList
from ipywidgets_todo.store.todo_store import TodoStore


@pytest.fixture
def todo_list(todo_store: TodoStore) -> TodoList:
    return TodoList(store=todo_store)


@pytest.fixture(params=[("Input todo",)])
def todo_input_params(request: pytest.FixtureRequest) -> tuple:
    return request.param


def test_add_todo(
    todo_list: TodoList,
    todo_store: TodoStore,
    todo_input_params: tuple,
    todo_store_params: tuple,
) -> None:
    old_todo_count = len(todo_store.todos)
    todo_list.new_todo_input.value = todo_input_params[0]
    todo_list.add_todo()
    new_todo_count = len(todo_store.todos)
    assert new_todo_count == old_todo_count + 1
    assert todo_store.todos[new_todo_count - 1].text == todo_input_params[0]
    assert todo_store.todos[new_todo_count - 1].completed is False
    assert todo_list.new_todo_input.value == ""
    assert todo_store.todos[0].text == todo_store_params[0]
    assert todo_store.todos[0].completed is todo_store_params[1]


def test_add_empty_todo(todo_list: TodoList, todo_store: TodoStore) -> None:
    old_todo_count = len(todo_store.todos)
    todo_list.new_todo_input.value = ""
    with pytest.raises(ValueError) as e:
        todo_list.add_todo()
    new_todo_count = len(todo_store.todos)
    assert str(e.value) == "Todo text must be a non-empty string"
    assert new_todo_count == old_todo_count
