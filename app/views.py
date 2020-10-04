from flask import Flask, render_template, url_for, request
from config import API_KEY

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    user_message = request.args.get('ask')
    return render_template('index.html',
                            gp_welcome = url_for('static',
                                filename = 'img/hello.png'),
                            gp_searching = url_for('static',  
                                filename = 'img/searching.png'),
                            gp_found = url_for('static',
                                filename = 'img/found.png'),
                            gp_not_found = url_for('static',
                                filename = 'img/not_found.png'),
                            trombi = url_for('static',
                                filename = 'img/trombi.png'),
                            script = url_for('static',
                                filename = 'js/requests.js'),
                            ask = user_message,
                            map_key = API_KEY,
                            bot_message = None)

@app.route('/about_me/')
def about_me():
    return render_template('about_me.html')

@app.route('/about_app/')
def about_app():
    return render_template('about_app.html')