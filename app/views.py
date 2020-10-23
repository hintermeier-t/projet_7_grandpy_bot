import os
import random
import dotenv

from flask import Flask, render_template, url_for, request

from .py_app import *

app = Flask(__name__)

dotenv.load_dotenv(os.path.join("", ".env"))
gmaps_key = os.getenv("GMAPS_API_KEY")


@app.route('/')
@app.route('/index/')
def index():
    ran = random.randint(1,3)
    question = request.args.get('u_message')
    if request.args.get('u_message') is None:
        question = None
        answer = None
        message = None
    else:
        message = query.Query(request.args.get('u_message'))
        answer = message.response

    data = {"user_message":question, "py_message":answer}

    return render_template('index.html',
                            script = url_for('static',
                                filename = 'js/script.js'),
                            grandpy = url_for('static',
                                filename = 'img/grandpy_'+str(ran)+'.png'),
                            key = gmaps_key,
                            maps_result= None,
                            data=data)
@app.route("/question/")
def response():

    query = Query(request.args.get("u_input"))
    partial_answer = Answer(query.response)
    complete_answer = partial_answer.construct()
    return complete_answer

#- Optionnal pages

@app.route('/about_me/')
def about_me():
    return render_template('about_me.html')

@app.route('/about_app/')
def about_app():
    return render_template('about_app.html')
