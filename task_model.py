import sqlite3


def create_db(db_filename):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE tasks
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               done BOOLEAN NOT NULL)
        '''
    )
    conn.commit()
    conn.close()


def to_dict(row):
    return {'id': row[0], 'title': row[1], 'done': bool(row[2])}


def get_tasks(db_filename):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    task = [to_dict(task) for task in cursor.fetchall()]
    conn.close()
    return task


def get_task_by_id(task_id, db_filename):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    conn.close()
    return to_dict(task)


def add_task(title, db_filename):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, done) VALUES (?, ?)', (title, False))
    conn.commit()
    task_id = cursor.lastrowid

    # get last added task with id
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    conn.close()

    return to_dict(task)


def update_task(task_id, new_title, new_done, db_filename):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET title = ?, done = ? WHERE id = ?',
                   (new_title, new_done, task_id))
    conn.commit()

    # get last added updated task
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    conn.close()

    return to_dict(task)


if __name__ == "__main__":
    # testing
    db_filename = "t.db"
    create_db(db_filename)
    add_task("Task A", db_filename)
    add_task("Task B", db_filename)
    add_task("Task C", db_filename)
    print(get_tasks(db_filename))
    task = get_task_by_id(2, db_filename)
    print(task)
    print(update_task(2, "NEW TITLE", True, db_filename))
    print(get_tasks(db_filename))
