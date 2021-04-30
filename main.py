class MarksList:
    """
    List of marks of study subject
    """
    subjectTitle: str
    marks = []

    def __init__(self, subjectTitle: str, marks):
        self.subjectTitle = subjectTitle
        self.marks = marks

    def predict(self, mark_to_add, mark_aim):
        """
        Returns the number of `mark_to_add` needed to get the `final_mark` equal `mark_aim` 
        """
        temp_list = MarksList("", self.marks)
        count = 0
        while True:
            if temp_list.final_mark == mark_aim:
                return count
            temp_list.marks.append(mark_to_add)
            count += 1

    @property
    def average(self):
        """
        Arithmetic mean of marks
        """
        return sum(self.marks) / len(self.marks)

    @property
    def final_mark(self):
        """
        The rounded arithmetic mean of marks 
        """
        average = self.average
        fractional_part = average - int(average)
        return int(average) if (fractional_part) < 0.5 else (int(average) + 1)


class Parser:

    def parseLine(self, text: str) -> MarksList:
        """
        Line format:

        `Subject Name`{space}`marks`
        * Subject name can contain any characters including spaces
        * marks must be without any characters, example: 3542354354
        """
        try:
            subjectTitle = ' '.join(text.split(' ')[0:-1:])
            marks = list(map(lambda x: int(x), text.split(' ')[-1]))

            return MarksList(subjectTitle, marks)
        except:
            return None
