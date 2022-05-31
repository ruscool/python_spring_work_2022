import psycopg2 as ps


class DB:
    __instance__ = None

    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password
        if DB.__instance__ is None:
            DB.__instance__ = self
        else:
            raise Exception("We can not creat another class")

    @staticmethod
    def get_instance():
        # We define the static method to fetch instance
        if not DB.__instance__:
            DB()
        return DB.__instance__

    def get_connection(self):
        with ps.connect(f"dbname={self.name} user={self.user} password={self.password}") as self.conn:
            with self.conn.cursor() as cur:
                cur.execute(f"""SELECT *  FROM profile
                    """)
                res = cur.fetchall()

        return self.conn


dbb = DB('testsystem', 'testsystem', '1234test')
print(dbb.get_connection())
print(dbb.__class__)

# class Db:
#     def __init__(self, name, user, password):
#         self.name = name
#         self.user = user
#         self.password = password
#
#     def get_connection(self):
#         with ps.connect(f"dbname={self.name} user={self.user} password={self.password}") as self.conn:
#             with self.conn.cursor() as cur:
#                 cur.execute(f"""SELECT *  FROM profile
#                     """)
#                 res = cur.fetchall()
#
#         return self.conn
