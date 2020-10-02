"""
    Parser module containing the class
"""
import os
import unidecode
class Parser:
    """
        Parser class that will clean a string by :
            -Removing emphasis;
            -Removing uppercases;
            -Removing separators;
            -Removing "stop words".
    Attributes :
    ------------
    :self.separators (list): a list containing every punctuation
    :self.stop_words (list): a liste containing tons of French stop words to
        remove before sending the request.
    
    Methods:
    --------
    :deemphasize(self, string): remove emphased letters from the string.
    :lower_all(self, string): turn uppercases into lowercases.
    :depunctuate(self, string): remove punctuation from the string.
    :clarify(self, string): remove every useless word to keep the string
        as relevant as possible.
    """
    def __init__(self, *string):
        rawfile = open("../static/res/stop_words.txt", 'r')
        self.stop_words = [line.split(",") for line in rawfile][0]
        rawfile.close()
        self.separators = "!\"#$%&'()*+, -./:;<=>?@[\\]^_`{|}~"

    def lower_all(self,string):
        return string.lower()
    
    def unmark(self, string):
        return string.strip(self.separators)

    def deemphasize(self,string):
        return unidecode.unidecode(string)
    
    def cleanup(self, string):
        listing = string.split(" ")
        listing = [word for word in listing if word not in self.stop_words]
        return ' '.join(listing)