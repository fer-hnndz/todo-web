from flask import render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from todo.forms import AddTaskForm, DeleteTaskForm, RegisterForm, LoginForm
from todo import app
from todo.models import Task, Users
from todo import db
import traceback


@app.route('/', methods=['GET', 'POST'])
def index():
    if not (current_user.is_authenticated):
        return redirect(url_for('login'))

    add_task_form = AddTaskForm()
    delete_task_form = DeleteTaskForm()

    if add_task_form.validate_on_submit():

        try:
            task = Task(task_name=add_task_form.task_name.data, owner_id=current_user.id,
                        due_date=add_task_form.due_date.data, due_time=add_task_form.due_time.data)

            db.session.add(task)
            db.session.commit()

            flash('Task added successfully!', 'success')

        except Exception as e:
            flash('There was an error while adding the task.', 'danger')
            traceback.print_exc()

        return redirect(url_for('index'))

    tasks = Task.query.filter_by(
        owner_id=current_user.id).order_by(Task.id.desc()).all()
    return render_template('index.html', add_task_form=add_task_form, delete_task_form=delete_task_form, tasks=tasks)


@app.route('/tasks/delete/<int:task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    try:
        task_obj = Task.query.filter_by(id=task_id).first()

        if task_obj is None:
            flash('Could not find that task :(', 'danger')

        else:
            db.session.delete(task_obj)
            db.session.commit()

            flash('Task deleted successfully!', 'success')
            redirect(url_for('index'))

    except Exception as e:
        flash('There was an error while deleting the task.', 'danger')
        print(traceback.print_exc())

    return redirect(url_for('index'))

# * Login System


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = Users.query.filter_by(username=username).first()

        if user is not None:
            login_user(user)
            return redirect(url_for('index'))

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    register_form = RegisterForm()

    if register_form.validate_on_submit():
        try:

            username = register_form.username.data
            password = register_form.password.data

            # Check if username is talen

            user = Users.query.filter_by(username=username).first()

            if user is None:
                user = Users(username=username, password=password)
                db.session.add(user)
                db.session.commit()

                flash(
                    'You have successfully registered! Please log in to your account.', 'success')

                return redirect(url_for('login'))

            else:
                flash('That username is already taken.', 'danger')

        except Exception as e:
            flash(e, 'danger')

    return render_template('register.html', register_form=register_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
