from app import db

class KanbanCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    column = db.Column(db.String(20))
