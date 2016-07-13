from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	taskname = db.Column(db.Text)
	taskdescription = db.Column(db.Text)
	taskpriority =  db.Column(db.Text)
	taskdate =  db.Column(db.Text)
	projectname =  db.Column(db.Text)
	status = db.Column(db.Text)

	def __init__(self,taskname,taskdescription,taskpriority,taskdate,projectname,status):
		self.taskname = taskname
		self.taskdescription = taskdescription
		self.taskpriority = taskpriority
		self.taskdate = taskdate
		self.projectname = projectname
		self.status = status

db.create_all()

@app.route("/")
def hello_world():
	tasks = Task.query.all()
	return render_template('list.html',tasks=tasks)

@app.route("/update", methods=['POST'])
def update():
	editid=request.form['taskid']
	update=Task.query.get(editid)
	update.taskname =request.form['taskname']
	update.taskdescription = request.form['taskdescription']
	update.taskpriority = request.form['taskpriority']
	update.taskdate = request.form['taskdate']
	update.projectname = request.form['projectname']
	update.status = request.form['status']

	# task = Task(taskname,taskdescription,taskpriority,taskdate,projectname,status)
	
	# db.session.add(task)
	db.session.commit()
	return redirect("/")
	

@app.route("/delete/<int:task_id>")
def del_task(task_id):
	task_del = Task.query.get(task_id)
	db.session.delete(task_del)
	db.session.commit()
	return redirect("/")

@app.route("/add", methods=["POST"])
def add_task():
	taskname =request.form['taskname']
	taskdescription = request.form['taskdescription']
	taskpriority = request.form['taskpriority']
	taskdate = request.form['taskdate']
	projectname = request.form['projectname']
	status = request.form['status']

	task = Task(taskname,taskdescription,taskpriority,taskdate,projectname,status)
	
	db.session.add(task)
	db.session.commit()
	return redirect("/")

@app.route("/edit/<int:task_id>", methods=["GET"])
def editing(task_id):
	task_edit = Task.query.get(task_id)
	return render_template('edit.html',update=task_edit)

if __name__ == "__main__":
	app.run(debug=True)
