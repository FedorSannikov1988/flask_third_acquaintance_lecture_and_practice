from flask import Flask
from models_1_lecture_3 import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'This is the main page'


if __name__ == '__main__':
    app.run()
