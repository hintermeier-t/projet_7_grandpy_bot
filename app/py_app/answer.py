# coding:utf-8
#- Import standard modules
import random as r
import json

class Answer:
    def __init__(self, answer):
        self.json_answers = answer
        rawfile = open("app/static/res/answers.txt", 'r')
        self.py_answers = [line.split(",") for line in rawfile][0]
        rawfile.close()
        self._construct()

    def _construct (self):
        randint = r.randint(1, len(self.py_answers))
        self.json_answers.update(
            {"intro": str(self.py_answers[randint-1])})
