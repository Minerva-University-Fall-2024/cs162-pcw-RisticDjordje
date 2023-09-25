from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import KanbanCard
from app.routes import bp

@app.route('/')
def index():
    columns = ['To Do', 'In Progress', 'Review', 'Testing', 'Done']
    cards = {column: KanbanCard.query.filter_by(column=column).all() for column in columns}
    return render_template('kanban.html', columns=columns, cards=cards)

@app.route('/add_card', methods=['POST'])
def add_card():
    title = request.form.get('title')
    description = request.form.get('description')
    column = request.form.get('column')
    
    if title and column:
        new_card = KanbanCard(title=title, description=description, column=column)
        db.session.add(new_card)
        db.session.commit()
        flash('Card added successfully', 'success')
    else:
        flash('Card title and column are required', 'error')
    
    return redirect(url_for('index'))

@app.route('/move_card/<int:card_id>/<new_column>')
def move_card(card_id, new_column):
    card = KanbanCard.query.get_or_404(card_id)
    card.column = new_column
    db.session.commit()
    return redirect(url_for('index'))
