from todo import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    due_time = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return f"Task('{self.name}', '{self.due_date}', '{self.due_time}')"

    def get_date_label(self):
        # Make a dict of numbers with month
        month = {'01': 'January',
                 '02': 'February',
                 '03': 'March',
                 '04': 'April',
                 '05': 'May',
                 '06': 'June',
                 '07': 'July',
                 '08': 'August',
                 '09': 'September',
                 '10': 'October',
                 '11': 'November',
                 '12': 'December'}

        month_index = f"{self.due_date.month:02}"
        output = f'{month[month_index]} {self.due_date.day}, {self.due_date.year} @ {self.due_time.hour}:{self.due_time.minute}'

        return output
