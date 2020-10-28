#- Import standard modules
import random as r

class Answer:
    def __init__(self, answer):
        self.json_answers = answer
        rawfile = open("app/static/res/answers.txt", 'r')
        self.py_answers = [line.split(",") for line in rawfile][0]
        rawfile.close()

    def construct (self):
        randint = r.randint(0, len(self.py_answers))
        return self.json_answers.update({"intro": self.py_answers[randint]})
