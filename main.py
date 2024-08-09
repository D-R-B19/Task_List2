import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, json
from logger import setup_logger

VISITS_FILE = 'visits.json'
app = Flask(__name__)
log = setup_logger("app")

# Initial list of tasks
tasks = []

@app.route('/')
def index():
    log.info('function tasks called')
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    if task.strip():
        tasks.append(task.strip())
    return redirect(url_for('index'))

@app.route('/edit_task/<int:index>', methods=['POST'])
def edit_task(index):
    new_task = request.form['new_task']
    if new_task.strip():
        tasks[index] = new_task.strip()
    return redirect(url_for('index'))

@app.route('/delete_task/<int:index>', methods=['POST'])
def delete_task(index):
    log.info('function tasks called')
    del tasks[index]
    return redirect(url_for('index'))

# Visit count
def get_visit_count():
    if not os.path.exists(VISITS_FILE):
        return 0
    with open(VISITS_FILE, 'r') as f:
        data = json.load(f)
        return data.get('visits', 0)

def increment_visit_count():
    visitor = get_visit_count() + 1
    with open(VISITS_FILE, 'w') as f:
        json.dump({'visits': visitor}, f)

@app.route('/visits')
def visits():
    visits = get_visit_count()
    return jsonify({"visits": visits})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)