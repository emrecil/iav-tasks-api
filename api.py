import os.path

from flask import Flask, request, jsonify
import task_model

app = Flask(__name__)

db_filename = os.environ.get('DATABASE_PATH', 'tasks.db')

if not os.path.exists(db_filename):
    task_model.create_db(db_filename)


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        all_tasks = task_model.get_tasks(db_filename)
        return jsonify(all_tasks), 200

    elif request.method == 'POST':
        new_task = request.json
        if 'title' in new_task:
            added_task = task_model.add_task(new_task['title'], db_filename)
            return jsonify(added_task), 201
        else:
            return 'Bad Request: Missing title', 400


@app.route('/task/<int:task_id>', methods=['GET', 'POST'])
def task(task_id):
    if request.method == 'GET':
        existing_task = task_model.get_task_by_id(task_id, db_filename)
        if existing_task:
            return jsonify(existing_task)
        else:
            return 'Task not found', 404

    elif request.method == 'POST':
        updated_task = request.json
        if 'title' in updated_task and 'done' in updated_task:
            added_task = task_model.update_task(task_id, updated_task['title'], updated_task['done'], db_filename)
            return jsonify(added_task), 200
        else:
            return 'Bad Request: Missing title or done', 400
