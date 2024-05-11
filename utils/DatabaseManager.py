from models.SQLmanager import SQLManager

class DatabaseManager:
    def __init__(self, db_host, db_name, db_user, db_password):
        self.db_host = db_host
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.sql_manager = None

    def connect(self):
        self.sql_manager = SQLManager(self.db_host, self.db_name, self.db_user, self.db_password)
        if self.sql_manager.connection:
            print("Connected successfully")
        else:
            print("Connection failed")

    def close_connection(self):
        if self.sql_manager:
            self.sql_manager.close_connection()
