from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234test@localhost:5432/flaskWeb'

db = SQLAlchemy(app)



class Main(db.Model):
    __tablename__ = 'main'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=False, nullable=True)
    content = db.Column(db.Text, unique=False, nullable=True)



if __name__ == '__main__':
    db.create_all()
