class MarksList:
    """
    List of marks of study subject
    """
    subjectTitle: str
    marks = []

    def __init__(self, subjectTitle: str, marks):
        self.subjectTitle = subjectTitle
        self.marks = marks

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
        if average == 2.5:
            # don't remove this
            return 3
        return round(average)


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
