from traitlets import Bool, HasTraits, List, Unicode, validate


class Todo(HasTraits):
    """A Todo item.
    Args:
        text (str): The text for the Todo item.
        completed (bool): The completion status.
    """

    text = Unicode()
    completed = Bool()

    @validate("text")
    def _validate_text(self, proposal: dict) -> str:
        if not len(proposal["value"]) > 0:
            raise ValueError("Todo text must be a non-empty string")
        return proposal["value"]


class TodoStore(HasTraits):
    """The Store for Todo items.
    Args:
    """

    todos = List(list[Todo]())

    def add_todo(self, text: str, completed: bool = False) -> Todo:
        """Add a new Todo item to the store.
        Args:
            text (str): The text for the new Todo item.
            completed (bool, optional): The completion status. Defaults to False.
        Returns:
            Todo: The newly created Todo object.
        """

        new_todo = Todo(text=text, completed=completed)
        self.todos = self.todos + [new_todo]
        return new_todo

    def remove_todo(self, index: int) -> None:
        """Remove a Todo item from the store by index.

        Args:
            index (int): The index of the Todo item to remove.

        Raises:
            IndexError: If the index is out of bounds.
        """

        if index < 0 or index >= len(self.todos):
            raise IndexError("Index out of range")
        self.todos = [todo for idx, todo in enumerate(self.todos) if idx != index]

    def toggle_todo(self, index: int) -> Todo:
        """Toggle the completion status of a Todo item by index.

        Args:
            index (int): The index of the Todo item to toggle.

        Returns:
            Todo: The updated Todo object.

        Raises:
            IndexError: If the index is out of bounds.
        """

        if index < 0 or index >= len(self.todos):
            raise IndexError("Index out of range")
        todo = self.todos[index]
        todo.completed = not todo.completed
        self.todos[index] = todo
        return todo


todo_store = TodoStore()
