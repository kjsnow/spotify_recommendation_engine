import sqlite3
import os

# conn = sqlite3.connect('todo.db')
# query = ''
# result = conn.execute(query)

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect(os.path.realpath('./data/todo2.db'))
        self.create_user_table()
        self.create_to_do_table()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

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

class ToDoModel:

    def __init__(self):
        self.conn = sqlite3.connect(os.path.realpath('./data/todo3.db'))
        #self.conn = sqlite3.connect('todo.db')
        self.TABLENAME = 'todo'

    def list_tables(self):
        query = '''select name from sqlite_master
                    where type="table"
                    order by name;
                '''
        result = self.conn.execute(query)
        return result

    def create(self, text, description):
        query = f'''insert into {self.TABLENAME} (title, description)
                    values ("{text}", "{description}")
                '''
        result = self.conn.execute(query)
        return result

    def select_all(self, table):
        query = f'''select * from {table}'''
        result = self.conn.execute(query)
        return result

    def select(self, text):
        query = f'''select * from {self.TABLENAME} where title = "{text}"'''
        result = self.conn.execute(query)
        return result

    def delete(self, text):
        query = f'''delete from {self.TABLENAME} where title = "{text}"'''
        result = self.conn.execute(query)
        return result

    def update(self, text, new_text):
        query = f'''update {self.TABLENAME}
                    set title = "{new_text}"
                    where title = "{text}"'''
        result = self.conn.execute(query)
        return result
