class StudentTask:
    def __init__(self, title):
        self.title = title

    def get_info(self):
        return self.title


class Deadline(StudentTask):
    def __init__(self, title, date):
        super().__init__(title)
        self.date = date

    def get_info(self):
        return f"{self.title} - {self.date}"


class ScheduleItem(StudentTask):
    def __init__(self, day, subject, time):
        super().__init__(subject)
        self.day = day
        self.time = time

    def get_info(self):
        return f"{self.day} - {self.title} - {self.time}"