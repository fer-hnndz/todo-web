from importlib.resources import read_text
from flask import render_template, request, redirect, url_for, flash
from todo.forms import AddTaskForm, DeleteTaskForm
from todo import app
from todo.models import Task
from todo import db
import traceback


@app.route('/', methods=['GET', 'POST'])
def index():
    add_task_form = AddTaskForm()
    delete_task_form = DeleteTaskForm()

    if add_task_form.validate_on_submit():

        try:
            task = Task(task_name=add_task_form.task_name.data,
                        due_date=add_task_form.due_date.data, due_time=add_task_form.due_time.data)

            db.session.add(task)
            db.session.commit()

            flash('Task added successfully!', 'success')

        except Exception as e:
            flash('There was an error while adding the task.', 'danger')
            traceback.print_exc()

        return redirect(url_for('index'))

    if delete_task_form.validate_on_submit():

        task_id = delete_task_form.task_id.data

        try:
            task_obj = Task.query.filter_by(id=task_id).first()

            if task_obj is None:
                flash('Task not found.', 'danger')

            else:
                db.session.delete(task_obj)
                db.session.commit()

                flash('Task deleted successfully!', 'success')
                redirect(url_for('index'))

        except Exception as e:
            flash('There was an error while deleting the task.', 'danger')
            print(traceback.print_exc())

    return render_template('index.html', add_task_form=add_task_form, delete_task_form=delete_task_form, tasks=Task.query.order_by(Task.id.desc()).all())
