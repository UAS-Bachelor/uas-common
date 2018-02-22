from flask import Flask, render_template, url_for, request
import sys
import argparse
import time
from os import system
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:////static/login.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=time.strftime('%Y-%m-%d %H:%M:%S'))

# how to print the users in debug
def __repr__(self):
        return '<User {}>'.format(self.username) 
"""
@app.route('/login', methods=['GET','POST'])
def index():
#    if request.method == 'POST':
#        username = request.form['username']
#        password_candidate = request.form['password']
#        app.logger.info(username)
#        app.logger.info(password_candidate)
    return render_template('login.html')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5002,
                        help='specify which port to run this service on')
    args = parser.parse_args()
    args.prog = sys.argv[0].split('/')[-1].split('.')[0]

    print('Running {} service'.format(args.prog))
    system('title {} service on port {}'.format(args.prog, args.port))
    app.run(port=args.port, debug=True)