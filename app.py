from flask import Flask, request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Projects(db.Model):
    """Projects schema"""
    project_id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(20))
    active = db.Column(db.Boolean)

    def __init__(self, project, active):
        self.project_name = project
        self.active = active

    def __repr__(self):
        return '<Project {}>'.format(self.project_name)


class Tasks(db.Model):
    """Tasks Model"""
    task_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))
    task = db.Column(db.Text)
    status = db.Column(db.Boolean, default=False)

    def __init__(self, project_id, task, status=True):
        self.project_id = project_id
        self.task = task
        self.status = status

    def __repr__(self):
        return '<Task {}>'.format(self.task)


# initialize the database
db.create_all()


@app.route('/')
def index():
    """
    Home Route of the app

    """
    active = None
    projects = Projects.query.all()
    tasks = Tasks.query.all()

    if len(projects) == 1:
        projects[0].active = True
        active = projects[0].project_id
        db.session.commit()

    if projects:
        for project in projects:
            if project.active:
                active = project.project_id
        if not active:
            projects[0].active = True
            active = projects[0].project_id
    else:
        projects = None

    if projects:
        return render_template('index.html', tasks=tasks, projects=projects, active=active)
    else:
        return render_template('index.html', tasks=tasks, active=active)


@app.route('/add', methods=['POST'])
def add_task():
    """Addition a new task
    """
    found = False
    project_id = None
    task = request.form['task']
    project = request.form['project']
    
    if not task:
        return redirect('/')

    if not project:
        project = 'Tasks'

    projects = Projects.query.all()

    for proj in projects:
        if proj.project_name == project:
            found = True

    #Addition of project
    if not found:
        add_project = Projects(project, True)
        db.session.add(add_project)
        db.session.commit()
        projects = Projects.query.all()

    # Setting for active tab
    for proj in projects:
        if proj.project_name == project:
            project_id = proj.project_id
            proj.active = True
        else:
            proj.active = False

    status = bool(int(request.form['status']))

    # Addition of new task
    new_task = Tasks(project_id, task, status)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')


@app.route('/close/<int:task_id>')
def close_task(task_id):
    """
    Changing the Status of a task
    """
    task = Tasks.query.get(task_id)

    if not task:
        return redirect('/')

    if task.status:
        task.status = False
    else:
        task.status = True

    db.session.commit()
    return redirect('/')


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Deletes task by its ID

    """
    task = Tasks.query.get(task_id)

    if not task:
        return redirect('/')

    db.session.delete(task)
    db.session.commit()
    return redirect('/')


@app.route('/clear/<delete_id>')
def clear_all(delete_id):
    """Destroys all tasks from the An Active Project and removes its tab too"""
    Tasks.query.filter(Tasks.project_id == delete_id).delete()
    Projects.query.filter(Projects.project_id == delete_id).delete()
    db.session.commit()

    return redirect('/')


@app.route('/remove/<lists_id>')
def remove_all(lists_id):
    """Destroys All Tasks From An Active Project"""
    Tasks.query.filter(Tasks.project_id == lists_id).delete()
    db.session.commit()

    return redirect('/')


@app.route('/project/<tab>')
def tab_nav(tab):
    """For Projects Switching"""
    projects = Projects.query.all()

    for project in projects:
        if project.project_name == tab:
            project.active = True
        else:
            project.active = False

    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
