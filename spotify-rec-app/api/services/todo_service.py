from ..models.todo_model import ToDoModel

class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        return self.model.create(params['title'], params['description'])

    def select(self, params):
        return self.model.select_all(params['table'])

    def list_tables(self):
        return self.model.list_tables()