# todo: Создайте простое  приложение с помощью статьи:
# How to Use One-to-Many Database Relationships with Flask-SQLAlchemy
# https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-sqlalchemy

from flask import Flask, render_template
from jinja2 import Template
from engine.conn_db import db, Main

app = Flask(__name__)

conn = db.create_all()

posts = Main.query.all()
for post in posts:
    print(post.title)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/news')
def news():
    return render_template('news.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
