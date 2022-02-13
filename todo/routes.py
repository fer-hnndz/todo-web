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

    elif delete_task_form.validate_on_submit():
        pass

    return render_template('index.html', add_task_form=add_task_form, delete_task_form=delete_task_form, tasks=Task.query.order_by(Task.id.desc()).all())
