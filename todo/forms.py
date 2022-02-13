from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import StringField, DateField, TimeField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    task_name = StringField('Task Name', validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[
                         DataRequired()])

    due_time = TimeField('Due Time', validators=[
                         DataRequired()])

    submit = SubmitField('Add Task')


class DeleteTaskForm(FlaskForm):
    task_id = IntegerField('Task ID', validators=[DataRequired()])

    submit = SubmitField('Delete Task')
