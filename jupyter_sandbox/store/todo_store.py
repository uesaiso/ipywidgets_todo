from traitlets import Bool, HasTraits, List, Unicode, validate


class Todo(HasTraits):
    text = Unicode()
    completed = Bool()

    @validate("text")
    def _validate_text(self, proposal: dict) -> str:
        if not len(proposal["value"]) > 0:
            raise ValueError("Todo text must be a non-empty string")
        return proposal["value"]


class TodoStore(HasTraits):
    todos = List(list[Todo]())

    def add_todo(self, text: str, completed: bool = False) -> Todo:
        new_todo = Todo(text=text, completed=completed)
        self.todos = self.todos + [new_todo]
        return new_todo

    def remove_todo(self, index: int) -> None:
        self.todos = [todo for idx, todo in enumerate(self.todos) if idx != index]

    def toggle_todo(self, index: int) -> Todo:
        todo = self.todos[index]
        todo.completed = not todo.completed
        self.todos[index] = todo
        return todo


todo_store = TodoStore()
