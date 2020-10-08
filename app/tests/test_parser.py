"""
    Script that tests the Parser class.
"""
from ..py_app.parser import Parser
import pytest

class TestParser:
#- Parser test class
    UPPERCASES = "Ceci est un TEST DE MAJUSCULES"
    MARKS = "ceci, est un test; mais. de ponctuation ?!"
    EMPHASIS = "éèêâàôùîç"
    SENTENCE = "ou est OpenClassrooms"
    FINAL_SENTENCE = "Où est Openclassrooms, s'il te plaît ?"
    CLEANER = Parser()

    #- All uppercases are turned into lowercases
    def test_lower_all(self):        
        lowercases = self.CLEANER.lower_all(self.UPPERCASES)
        assert lowercases == "ceci est un test de majuscules"

    #- Remove punctuation
    def test_unmark(self):
        unmarked = self.CLEANER.unmark(self.MARKS)
        assert unmarked == "ceciestuntestmaisdeponctuation"

    #- Remove empasis
    def test_deemphasize(self):
        deemphasized = self.CLEANER.deemphasize(self.EMPHASIS)
        assert deemphasized == "eeeaaouic"

    #- Remove every undesired word
    def test_cleanup(self):
        cleaned_string = self.CLEANER.cleanup(self.SENTENCE)
        assert cleaned_string == "OpenClassrooms"

    #- Final parsing test (Combination of all Parser class methods)
    def test_parse(self):
        parsed_sentence = self.CLEANER.parse(self.FINAL_SENTENCE)
        assert parsed_sentence == "openclassrooms"