import unittest

from main import *


class Tests(unittest.TestCase):
    def test_parse_line(self):
        test_cases = [
            ["Subject 123", "Subject", [1, 2, 3]],
            ["Subject Title 123456", "Subject Title", [1, 2, 3, 4, 5, 6]],
            ["my subj name 2534", "my subj name", [2, 5, 3, 4]]
        ]
        self.parser = Parser()

        for test in test_cases:
            input_text = test[0]
            subjectTitle = test[1]
            marks = test[2]

            parsedLine = self.parser.parseLine(input_text)

            self.assertEqual(parsedLine.subjectTitle, subjectTitle)
            self.assertEqual(parsedLine.marks, marks)
