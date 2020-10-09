import os
import random
import dotenv

from flask import Flask, render_template, url_for, request

app = Flask(__name__)

dotenv.load_dotenv(os.path.join("", ".env"))
gmaps_key = os.getenv("GMAPS_API_KEY")


@app.route('/')
@app.route('/index/')
def index():
    ran = random.randint(1,3)
    user_message = request.args.get('ask')
    return render_template('index.html',
                            grandpy = url_for('static',
                                filename = 'img/grandpy_'+str(ran)+'.png'),
                            ask = user_message,
                            key = gmaps_key,
                            maps_result= None,
                            bot_message = None)


#- Optionnal pages

@app.route('/about_me/')
def about_me():
    return render_template('about_me.html')

@app.route('/about_app/')
def about_app():
    return render_template('about_app.html')