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

    def test_average_mark(self):
        test_cases = [
            [[5, 2], 3.5],
            [[2, 2, 3, 3], 2.5],
            [[5, 2, 3, 4, 4], 3.6],
        ]
        for test in test_cases:
            marks_input = test[0]
            average = test[1]

            marks = MarksList("", marks_input)
            self.assertEqual(marks.average, average)

    def test_final_mark(self):
        test_cases = [
            [[5, 2], 4],
            [[2, 2, 3, 3], 3],
            [[5, 2, 3, 4, 4], 4],
            [[5, 2, 5, 5, 5, 5], 5]
        ]
        for test in test_cases:
            marks_input = test[0]
            final_mark = test[1]

            marks = MarksList("", marks_input)
            self.assertEqual(marks.final_mark, final_mark)

    def test_predict(self):
        test_cases = [
            [[5, 2], 5, 5, 4],
            [[5, 2], 3, 3, 1],
            [[5, 2], 2, 3, 1],
            [[5, 2], 2, 2, 5],

            [[2, 2, 3, 3], 4, 4, 8],
            [[2, 2, 3, 3], 5, 4, 3],
            [[2, 2, 3, 3], 5, 5, 16],
            [[2, 2, 3, 3], 2, 2, 1],

            [[5, 2, 3, 4, 4], 5, 5, 9],
            [[5, 2, 3, 4, 4], 2, 2, 12],
            [[5, 2, 3, 4, 4], 3, 3, 2],
            [[5, 2, 3, 4, 4], 2, 3, 1]
        ]
        for test in test_cases:
            marks_input = test[0]
            mark_to_add = test[1]
            mark_aim = test[2]
            result_expected = test[3]

            marks = MarksList("", marks_input)
            self.assertEqual(marks.predict(
                mark_to_add, mark_aim), result_expected)
