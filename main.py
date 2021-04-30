import locale


class LocalStrings:
    language_index: int

    def __init__(self, language_index: int):
        self.language_index = language_index
        self._line_read_error = [
            "Ошибка во время чтения строки", "Error while reading line"]
        self._current_marks = ["Текущие оценки", "Current marks"]
        self._count = ["Количество", "Count of"]
        self._to = ["до", "to"]

    @property
    def current_marks(self):
        return self._current_marks[self.language_index]

    @property
    def line_read_error(self):
        return self._line_read_error[self.language_index]

    @property
    def count(self):
        return self._count[self.language_index]

    @property
    def to(self):
        return self._to[self.language_index]


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
        if self.final_mark < mark_aim:
            # going to better mark
            if mark_to_add < mark_aim:
                # impossible
                return 0
        else:
            # going to bad mark
            if mark_to_add > mark_aim:
                # impossible
                return 0

        temp_list = MarksList("", self.marks.copy())
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


def get_lang():
    if 'ru' in locale.getdefaultlocale()[0]:
        return 0
    else:
        return 1


def print_row_statistics(row: MarksList):
    for mark_to_add in range(2, 6):
        for mark_aim in range(2, 6):
            marks_count_to_aim = row.predict(mark_to_add, mark_aim)
            if marks_count_to_aim == 0:
                # it is not corrent, so skip this
                continue
            print(
                f'{local.count} \"{mark_to_add}\" {local.to} \"{mark_aim}\": {marks_count_to_aim}')


parser = Parser()
local = LocalStrings(get_lang())
file_lines = open('marks.txt').readlines()
marks_rows = []

for line in file_lines:
    line = line.strip()
    if line == '':
        continue
    current_marks = parser.parseLine(line)
    if current_marks == None:
        print(f'{local.line_read_error}: \"{line}\"')
        input()
        exit(0)
    marks_rows.append(current_marks)

for row in marks_rows:
    print(row.subjectTitle)
    current_marks = ', '.join(list(map(lambda x: str(x), row.marks)))
    print(f'{local.current_marks}: {current_marks}')
    print_row_statistics(row)
    print()
