# from Model.database import DataBase


class LoginScreenModel:
    def __init__(self, database):
        self.database = database

    def select_all_users(self):
        db = self.database
        cur = db.cursor()
        cur.execute("SELECT * from user;")
        u = cur.fetchall()
        print(u)

        # self.creat_user_table()

    # def validate_user_login_cridentials(self):
    #     return self.database.get_database_connection()

    # def creat_user_table(self):
    #     conn = self.database.get_database_connection()

    #     cur = conn.cursor()
    #     cur.execute(
    #         """CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTOINCREMENT);"""
    #     )
