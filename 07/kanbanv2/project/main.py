from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import User


main = Blueprint('main', __name__)

@main.route('/')
def index():
    columns = ['To Do', 'In Progress', 'Review', 'Testing', 'Done']
    tasks = {column: User.query.filter_by(column=column).all() for column in columns}
    return render_template('kanban.html', columns=columns, tasks=tasks)


# @main.route('/profile')
# @login_required
# def profile():
#     return render_template('index.html', name=current_user.name)

@main.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form.get('task-name')
    task_description = request.form.get('task-description')
    task_column = request.form.get('task-column')

    if task_name and task_column:
        new_task = User(name=task_name, description=task_description, column=task_column)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('main.index'))


# Endpoint to handle card move
@main.route('/move-card', methods=['POST'])
def move_card():
    data = request.get_json()
    card_id = data['column']
    new_status = data['new_status']
    
    card = User.query.get(card_id)
    if card:
        card.status = new_status
        db.session.commit()