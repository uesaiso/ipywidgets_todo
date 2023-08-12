import pytest
from jupyter_sandbox.store.todo_store import TodoStore


@pytest.fixture(params=[("Test todo", False), ("Test todo", True)])
def todo_store_params(request: pytest.FixtureRequest) -> tuple:
    return request.param


@pytest.fixture
def todo_store(todo_store_params: tuple) -> TodoStore:
    todo_store = TodoStore()
    todo_store.add_todo(todo_store_params[0], todo_store_params[1])
    return todo_store
