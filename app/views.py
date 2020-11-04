# coding:utf-8

#- Standard modules
import os
import random
import json

#- Pypi modules
import dotenv
from flask import Flask, render_template, url_for, request

#- Custom Modules
from .py_app import query, answer


app = Flask(__name__)

dotenv.load_dotenv(os.path.join("", ".env"))
gmaps_key = os.getenv("GMAPS_API_KEY")


@app.route("/")
@app.route("/index/")
def index():
    """Generating main page"""
    ran = random.randint(1, 3)
    return render_template(
        "index.html",
        script=url_for("static", filename="js/script.js"),
        grandpy=url_for("static", filename="img/grandpy_" + str(ran) + ".png"),
        favicon=url_for("static", filename="img/bot.png"),
        key=gmaps_key,
    )


@app.route("/request/")
def response():
    """Generating the Pybot answer"""
    u_query = query.Query(request.args.get("u_input"))
    partial_answer = answer.Answer(u_query.response)
    complete_answer = partial_answer.json_answers
    complete_answer.update({"key": gmaps_key})
    return json.dumps(complete_answer)


# - Optionnal pages


@app.route("/about_me/")
def about_me():
    """Generating About Me page"""
    return render_template("about_me.html")


@app.route("/about_app/")
"""Generating About App page"""
def about_app():
    return render_template("about_app.html")

@app.errorhandler(404)
def page_not_found(error):
    """Handling 404 error : page not found""""
    return render_template("error.html"), 404