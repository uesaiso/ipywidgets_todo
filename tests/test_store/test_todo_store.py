import pytest
from jupyter_sandbox.store.todo_store import Todo, TodoStore


@pytest.fixture(params=[("Test todo", False), ("Test todo", True)])
def todo_params(request: pytest.FixtureRequest) -> tuple:
    return request.param


@pytest.fixture
def todo(todo_params: tuple) -> Todo:
    return Todo(text=todo_params[0], completed=todo_params[1])


def test_todo_text(todo: Todo, todo_params: tuple) -> None:
    assert todo.text == todo_params[0]


def test_todo_completed(todo: Todo, todo_params: tuple) -> None:
    assert todo.completed == todo_params[1]


@pytest.mark.parametrize("completed", [True, False])
def test_empty_todo(completed: bool) -> None:
    with pytest.raises(ValueError) as e:
        Todo(text="", completed=completed)
    assert str(e.value) == "Todo text must be a non-empty string"


@pytest.fixture
def todo_store() -> TodoStore:
    return TodoStore()


def test_add_todo(todo_store: TodoStore) -> None:
    todo_store.add_todo(text="Test todo")
    assert len(todo_store.todos) == 1
    assert todo_store.todos[0].text == "Test todo"
    assert todo_store.todos[0].completed is False


def test_toggle_todo(todo_store: TodoStore) -> None:
    todo_store.add_todo(text="Test todo")
    todo_store.toggle_todo(index=0)
    assert todo_store.todos[0].completed is True
    todo_store.toggle_todo(index=0)
    assert todo_store.todos[0].completed is False


def test_remove_todo(todo_store: TodoStore) -> None:
    todo_store.add_todo(text="Test todo")
    todo_store.remove_todo(index=0)
    assert len(todo_store.todos) == 0


def test_toggle_todo_index_error(todo_store: TodoStore) -> None:
    todo_store.add_todo(text="Test todo")
    with pytest.raises(IndexError) as e:
        todo_store.toggle_todo(index=1)
    assert str(e.value) == "Index out of range"


def test_remove_todo_index_error(todo_store: TodoStore) -> None:
    todo_store.add_todo(text="Test todo")
    with pytest.raises(IndexError) as e:
        todo_store.remove_todo(index=1)
    assert str(e.value) == "Index out of range"
