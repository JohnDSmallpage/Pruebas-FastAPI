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

    def read_all(self):
        with self.conn.cursor() as cur:
            data= cur.execute("""
            SELECT * FROM "users";
                        """)
            return data.fetchall()

    def read_one(self, email):
        with self.conn.cursor() as cur:
            data= cur.execute("""
            SELECT * FROM "users" WHERE email = %(email)s;
                        """, {"email": email})
            return cur.fetchone()
    
    def delete(self, email):
        with self.conn.cursor() as cur:
            cur.execute("""
            DELETE FROM "users" WHERE email = %(email)s;
                        """, {"email": email})
            self.conn.commit()
    
    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
            UPDATE "users" SET nombre = %(nombre)s, email = %(email)s, password = %(password)s WHERE email = %(email)s;
                        """, data)
            self.conn.commit()
    
  
    
    def __def__(self):
        self.conn.close()