from todo import db, login_manager
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(db.ForeignKey("users.id"))
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    due: Mapped[datetime] = mapped_column(nullable=False)

    def __repr__(self):
        return f"Task('{self.name}', '{self.due}')"

    def get_date_label(self):
        # # Make a dict of numbers with month
        # month = {
        #     "01": "January",
        #     "02": "February",
        #     "03": "March",
        #     "04": "April",
        #     "05": "May",
        #     "06": "June",
        #     "07": "July",
        #     "08": "August",
        #     "09": "September",
        #     "10": "October",
        #     "11": "November",
        #     "12": "December",
        # }

        # month_index = f"{self.due_date.month:02}"
        # output = f"{month[month_index]} {self.due_date.day}, {self.due_date.year} @ {self.due_time.hour}:{self.due_time.minute:02}"

        output = self.due.strftime("%d/%m/%Y @ %H:%M")

        return output


class Users(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.password}')"


class User(UserMixin):
    pass
