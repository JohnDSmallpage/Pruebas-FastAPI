import psycopg

class UserConnection:
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect(
                host="localhost",
                dbname="Prueba FastAPI",
                user="postgres",
                password="Boston99."
            )
        except Exception as e:
            print("I am unable to connect to the database")
            

        

    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
            INSERT INTO "users" ("nombre", "email", "password") VALUES (%(nombre)s, %(email)s, %(password)s);
                        """, data)
            self.conn.commit()
    
    def __def__(self):
        self.conn.close()