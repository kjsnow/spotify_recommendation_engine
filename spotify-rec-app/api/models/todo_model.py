import sqlite

# conn = sqlite3.connect('todo.db')
# query = ''
# result = conn.execute(query)

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()

    def create_to_do_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS "todo" (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            _is_done boolean,
            _is_deleted boolean,
            created_on Date DEFAULT CURRENT_DATE,
            due_date Date,
            user_id INTERGER FOREIGNKEY REFERENCES user(_id)
        );
        '''

        self.conn.execute(query)

    def create_user_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS "user" (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        );
        '''

        self.conn.execute(query)

    if __name__ == "__main__":
        Schema()
        app.run(debug=True)

class ToDoModel:
    TABLENAME = "TODO"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def create(self, text, description):
        query = f'''insert into {TABLENAME} (title, description)
                    values ("{text}", "{description}")
                '''
        result = self.conn.execute(query)
        return result

    def select(self, text):
        query = f'''select * from {TABLENAME} where title = "{text}"'''
        result = self.conn.execute(query)
        return result

    def delete(self, text):
        query = f'''delete from {TABLENAME} where title = "{text}"'''
        result = self.conn.execute(query)
        return result

    def update(self, text,new_text):
        query = f'''update {TABLENAME}
                    set title = "{new_text}"
                    where title = "{text}"'''
        result = self.conn.execute(query)
        return result
    