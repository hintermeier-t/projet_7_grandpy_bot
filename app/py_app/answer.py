# coding:utf-8
"""
    The answer module contains the Answer class, which generate
        the GrandPy's answer.
"""
# - Import standard modules
import random as r


class Answer:
    """
        Answer class that will generate an complete answer to send to the app.
    Attributes :
    ------------
    :self.json_answers (dict): a dictionnary containing the answer.
    :self.py_answers (list): a list containing every possible 
        Pybot's catch phrase.

    Methods:
    --------
    :_construct(self): Add the Pybot's catch phrase, to complete the answer.
    """
    def __init__(self, answer):
        """
        Class constructor. generate the entire answer by callin _construct() method.
        """
        self.json_answers = answer
        rawfile = open("app/static/res/answers.txt", "r")
        self.py_answers = [line.split(",") for line in rawfile][0]
        rawfile.close()
        self._construct()

    def _construct(self):
        """
        Chose a random sentence in the list (from file), and add it to the
        self.json_answers.
        """
        randint = r.randint(1, len(self.py_answers))
        self.json_answers.update({"intro": str(self.py_answers[randint - 1])})
