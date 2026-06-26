import sqlite3

DB_NAME = 'logbook_database.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS logbook(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     session_date TEXT NOT NULL,
                     duration_seconds INTEGER NOT NULL,
                     activity TEXT NOT NULL,
                     result TEXT NOT NULL,
                     action_plan NOT NULL 
                     )
        ''')

def insert_logbook(
        session_date,
        duration_seconds,
        activity,
        result,
        action_plan
        ):
    
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            INSERT INTO logbook
                     (
                        session_date,
                        duration_seconds,
                        activity,
                        result,
                        action_plan
                     )
                     VALUES (?, ?, ?, ?, ?)
        ''', (
            session_date,
            duration_seconds,
            activity,
            result,
            action_plan
        ))

def get_all_logbooks():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute('''
                           SELECT *
                           FROM logbook
                           ORDER BY id DESC
                           ''')
        return cur.fetchall()

def get_logbook_by_id(logbook_id):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute('''
                           SELECT *
                           FROM logbook
                           WHERE id = ?
                           ''', (logbook_id,))
        return cur.fetchone()
    
def update_logbook(
        logbook_id,
        activity,
        result,
        action_plan
):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            UPDATE logbook
            SET
                     activity = ?,
                     result = ?,
                     action_plan = ?
            WHERE id = ?
        ''', (
            activity,
            result,
            action_plan,
            logbook_id
        ))

def delete_logbook(logbook_id):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
                     DELETE FROM logbook
                     WHERE id = ?
                     ''', (logbook_id,))

def get_total_duration():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute('''
                           SELECT SUM(duration_seconds)
                           FROM logbook
                           ''')
        return cur.fetchone()[0] or 0
    