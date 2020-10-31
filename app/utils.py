from flask import Flask, render_template, url_for, request

def log_writer(text):
    text = request.args.get('u_message')
    with open("app/templates/log.html", "a") as file:
        file.write("<div class=\"messageLine\">"+text+"</div>")
        file.close()
