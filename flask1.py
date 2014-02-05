from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.debug = True
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)

class nipples(db.Model):
    __tablename__ = 'nipples'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))

    def __init__(self, name):
        self.name = name

@app.route('/')
def hello_world():
    name = 'mike'
    return 'hello' + name

@app.route('/nipples')
def suckNipples():
    tit = nipples.query.all()
    0/0
    return 'help'

if __name__ == '__main__':
    app.run()

