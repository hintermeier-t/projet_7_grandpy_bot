"""
    Script that tests the Parser class.
"""
from ..parser import Parser
import pytest

class TestParser:
#- Parser test class
    UPPERCASES = "Ceci est un TEST DE MAJUSCULES"
    MARKS = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    EMPHASIS = "éèêâàôùîç"
    SENTENCE = "ou est OpenClassrooms"
    CLEANER = Parser()

    #- All uppercases are turned into lowercases
    def test_lower_all(self):        
        lowercases = self.CLEANER.lower_all(self.UPPERCASES)
        assert lowercases == "ceci est un test de majuscules"

    #- Remove punctuation
    def test_unmark(self):
        unmarked = self.CLEANER.unmark(self.MARKS)
        assert unmarked == ""

    #- Remove empasis
    def test_deemphasize(self):
        deemphasized = self.CLEANER.deemphasize(self.EMPHASIS)
        assert deemphasized == "eeeaaouic"

    #Remove every undesired word
    def test_cleanup(self):
        cleaned_string = self.CLEANER.cleanup(self.SENTENCE)
        assert cleaned_string == "OpenClassrooms"