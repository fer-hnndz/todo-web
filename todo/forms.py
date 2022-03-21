from distutils.text_file import TextFile
from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import StringField, DateField, TimeField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length


class AddTaskForm(FlaskForm):
    task_name = StringField('Task Name', validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[
                         DataRequired()])

    due_time = TimeField('Due Time', validators=[
                         DataRequired()])

    submit = SubmitField('Add Task')


class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Delete Task')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(min=5, max=35)])

    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=5, max=100), EqualTo('confirm_password', message='Passwords must match.')])

    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired()])

    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Login')
