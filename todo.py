from flask import Flask,request
from pymongo import MongoClient
from flask_restful import Resource,Api
from bson.objectid import ObjectId
from bson.errors import InvalidId
from flask import render_template,redirect, url_for

client=MongoClient('localhost', 27017)
db=client.db1
names=db.todo
users=db.user
app = Flask(__name__)
api=Api(app)

class Task(Resource):
	def get(self):
		data=[]
		for task in names.find():
			task["_id"]=str(task["_id"])
			data.append(task)
		return data

	def post(self):
		taskname=request.values.get("taskname")
		taskdescription=request.values.get("taskdescription") 
		taskpriority=request.values.get("taskpriority")
		taskdate=request.values.get("taskdate")
		projectname=request.values.get("projectname")
		status=request.values.get("status")

		names.insert({ "taskname":taskname, "taskdescription":taskdescription, "taskpriority":taskpriority, "taskdate":taskdate ,"projectname":projectname, "status":status})
	 	return "insertd",200

	def delete(self):
		taskname=request.values.get("taskname")
		taskdescription=request.values.get("taskdescription") 
		taskpriority=request.values.get("taskpriority")
		taskdate=request.values.get("taskdate")
		projectname=request.values.get("projectname")
		status=request.values.get("status")

		names.remove({ "taskname":taskname, "taskdescription":taskdescription, "taskpriority":taskpriority, "taskdate":taskdate, "projectname":projectname, "status":status})

		return "deleted",300

	def put(self):
		taskname=request.values.get("taskname")
		taskdescription=request.values.get("taskdescription") 
		taskpriority=request.values.get("taskpriority")
		taskdate=request.values.get("taskdate")
		projectname=request.values.get("projectname")
		status=request.values.get("status")

		id=request.values.get("id")
		id =ObjectId(id)	
		names.update({"_id":id}, { "$set":{"taskname":taskname, "taskdescription":taskdescription, "taskpriority":taskpriority, "taskdate":taskdate, "projectname":projectname, "status":status}})
		return "updated",400

class user(Resource):
	def get(self):
		datas=[]
		for user in users.find():
			user["_id"]=str(user["_id"])
			datas.append(user)
		return datas

	def post(self):
		username=request.values.get("username")
		password=request.values.get("password")
		result = users.find({"username":username, "password":password}).count()
		if(result==0):
			users.insert({"username":username, "password":password})
			return "added",200
		else:
			return "hello %s" %username

	def delete(self):
		username=request.values.get("username")
		password=request.values.get("password")

		users.remove({"username":username, "password":password})
		return "removed",300

	def put(self):
		username=request.values.get("username")
		password=request.values.get("password")

		id=request.values.get("id")
		id =ObjectId(id)	
		users.update({"_id":id}, { "$set":{"username":username, "password":password}})
		return "updated",400

api.add_resource(Task,"/")
api.add_resource(user,"/user")

if __name__ == "__main__":
	app.run(debug=True)