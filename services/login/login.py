from flask import Flask, render_template, url_for, request
import os

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
    print('Running {} service'.format(os.path.basename(__file__).split('.')[0]))
    app.run(port=5002, debug=True)