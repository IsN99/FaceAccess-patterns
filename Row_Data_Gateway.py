import psycopg

# Empl_RDG

class Empl_RDG:
    conn = psycopg.connect(host="localhost", database="mydatabase", user="myusername", password="mypassword")

    def __init__(self, id=None, name=None, photo_path=None):
        self.id = id
        self.name = name
        self.photo_path = photo_path

    @staticmethod
    def get(id=None):
        with Empl_RDG.conn.cursor() as cur:
            if id:
                cur.execute("SELECT id, name, photo_path FROM employees WHERE id = %s", (id,))
            else:
                cur.execute("SELECT id, name, photo_path FROM employees")
            rows = cur.fetchall()
            employees = []
            for row in rows:
                employee = Empl_RDG(*row)
                employees.append(employee)
            return employees

    def insert(self):
        with Empl_RDG.conn.cursor() as cur:
            cur.execute("INSERT INTO employees (name, photo_path) VALUES (%s, %s) RETURNING id",
                        (self.name, self.photo_path))
            self.id = cur.fetchone()[0]
            Empl_RDG.conn.commit()

    def update(self):
        with Empl_RDG.conn.cursor() as cur:
            cur.execute("UPDATE employees SET name = %s, photo_path = %s WHERE id = %s",
                        (self.name, self.photo_path, self.id))
            Empl_RDG.conn.commit()

    def delete(self):
        with Empl_RDG.conn.cursor() as cur:
            cur.execute("DELETE FROM employees WHERE id = %s", (self.id,))
            Empl_RDG.conn.commit()


# Checkpoint_RDG

class Checkpoint_RDG:
    conn = psycopg.connect(host="localhost", database="mydatabase", user="myusername", password="mypassword")

    def __init__(self, id=None, access_zone=None):
        self.id = id
        self.access_zone = access_zone

    @staticmethod
    def get(id=None):
        with Checkpoint_RDG.conn.cursor() as cur:
            if id:
                cur.execute("SELECT id, access_zone FROM checkpoints WHERE id = %s", (id,))
            else:
                cur.execute("SELECT id, access_zone FROM checkpoints")
            rows = cur.fetchall()
            checkpoints = []
            for row in rows:
                checkpoint = Checkpoint_RDG(*row)
                checkpoints.append(checkpoint)
            return checkpoints

    def insert(self):
        with Checkpoint_RDG.conn.cursor() as cur:
            cur.execute("INSERT INTO checkpoints (access_zone) VALUES (%s) RETURNING id", (self.access_zone,))
            self.id = cur.fetchone()[0]
            Checkpoint_RDG.conn.commit()

    def update(self):
        with Checkpoint_RDG.conn.cursor() as cur:
            cur.execute("UPDATE checkpoints SET access_zone = %s WHERE id = %s",
                        (self.access_zone, self.id))
            Checkpoint_RDG.conn.commit()

    def delete(self):
        with Checkpoint_RDG.conn.cursor() as cur:
            cur.execute("DELETE FROM checkpoints WHERE id = %s", (self.id,))
            Checkpoint_RDG.conn.commit()

# Request_RDG

class Request_RDG:
    conn = psycopg.connect(host="localhost", database="mydatabase", user="myusername", password="mypassword")

    def __init__(self, id=None, date=None, result=None, image_path=None, checkpoint_id=None, employee_id=None):
        self.id = id
        self.date = date
        self.result = result
        self.image_path = image_path
        self.checkpoint_id = checkpoint_id
        self.employee_id = employee_id

    @staticmethod
    def get(id=None):
        with Request_RDG.conn.cursor() as cur:
            if id:
                cur.execute("SELECT id, date, result, image_path, checkpoint_id, employee_id FROM requests WHERE id = %s", (id,))
            else:
                cur.execute("SELECT id, date, result, image_path, checkpoint_id, employee_id FROM requests")
            rows = cur.fetchall()
            requests = []
            for row in rows:
                request = Request_RDG(*row)
                requests.append(request)
            return requests

    def insert(self):
        with Request_RDG.conn.cursor() as cur:
            cur.execute("INSERT INTO requests (date, result, image_path, checkpoint_id, employee_id) VALUES (%s, %s, %s, %s, %s) RETURNING id",
                        (self.date, self.result, self.image_path, self.checkpoint_id, self.employee_id))
            self.id = cur.fetchone()[0]
            Request_RDG.conn.commit()

    def update(self):
        with Request_RDG.conn.cursor() as cur:
            cur.execute("UPDATE requests SET date = %s, result = %s, image_path = %s, checkpoint_id = %s, employee_id = %s WHERE id = %s",
                        (self.date, self.result, self.image_path, self.checkpoint_id, self.employee_id, self.id))
            Request_RDG.conn.commit()

    def delete(self):
        with Request_RDG.conn.cursor() as cur:
            cur.execute("DELETE FROM requests WHERE id = %s", (self.id,))
            Request_RDG.conn.commit()


