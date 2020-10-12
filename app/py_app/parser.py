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
    def __init__(self, optionnal_string = ""):
        self.string = optionnal_string
        rawfile = open("app/static/res/stop_words.txt", 'r')
        self.stop_words = [line.split(",") for line in rawfile][0]
        rawfile.close()
        self.separators = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        self.string = self._parse(self.string)

    def _lower_all(self,string):
        return string.lower()

    def _unmark(self, string):
        return ''.join(char for char in string if char not in self.separators)

    def _deemphasize(self,string):
        return unidecode.unidecode(string)

    def _cleanup(self, string):
        listing = string.split(" ")
        listing = [word for word in listing if word not in self.stop_words]
        return ' '.join(listing)

    def _parse(self, string):
        """
            This method will parse a sentence to get only meaningful words.
        """
        string = self._lower_all(string)
        string = self._deemphasize(string)
        string = self._cleanup(string)
        string = self._unmark(string)
        return string
