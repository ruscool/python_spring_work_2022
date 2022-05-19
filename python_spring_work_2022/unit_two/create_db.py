import psycopg2 as ps

# Connect to an existing database
with ps.connect("dbname=my_base user=my_user") as conn:
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        # Execute a command: this creates a new table
        #
        # cur.execute("""CREATE TABLE "user" (
        #   "id_user" SERIAL PRIMARY KEY,
        #   "first_name" VARCHAR(255) NOT NULL,
        #   "ouch" VARCHAR(255) NOT NULL,
        #   "last_name" VARCHAR(255) NOT NULL,
        #   "age" SMALLINT,
        #   "dt_create" TIMESTAMP,
        #   "status" BOOLEAN
        #     );""")

        # cur.execute("""CREATE TABLE "profile" (
        #   "profile" SERIAL PRIMARY KEY,
        #   "id_users" INTEGER NOT NULL,
        #   "login" TEXT NOT NULL,
        #   "password" TEXT NOT NULL,
        #   "dt_reg" DATE,
        #   "avatar" TEXT NOT NULL,
        #   "dt_last_login" DATE,
        #   "status" BOOLEAN);
        #         """)

        # создание индекса
        # cur.execute(
        #     """CREATE INDEX "idx_profile__id_users" ON "profile" ("id_users");"""
        # )

        # констрейн
        # cur.execute("""
        # ALTER TABLE "profile" ADD CONSTRAINT "fk_profile__id_users" FOREIGN KEY ("id_users")
        # REFERENCES "user" ("id_user")
        # """)

        # добавление нового пользователя в таблицу User
        # cur.execute("""
        # INSERT INTO "user" (id_user,first_name,ouch,last_name,age,dt_create,status)
        # VALUES (3,'Петр','Иванович','Зуев',35,'2022-05-02 07:34:00',true);
        # """)

        # добавление в таблицу profile
        # cur.execute("""
        # INSERT INTO profile (id_users, login,"password",dt_reg, dt_last_login, status)
        # VALUES (3,'user_3','5678','2022-01-10 12:00:10','2022-04-12 22:15:10',true);
        # """)

        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM profile")
        res = cur.fetchall()
        for i in res:
            print(i)
        # # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # # of several records, or even iterate on the cursor
        conn.commit()
