from flask import Flask, render_template, url_for, request
import sys
import argparse
from os import system

app = Flask(__name__)


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