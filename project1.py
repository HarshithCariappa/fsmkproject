# import subprocess
# 	name of os
# 	no of partitions
# 	directory structurs
# 	disk usage details
# 	RAM usage details

from flask import Flask,request
from pymongo import MongoClient
from flask_restful import Resource,Api
from bson.objectid import ObjectId
from bson.errors import InvalidId
from flask import render_template,redirect, url_for

client=MongoClient('localhost', 27017)
db=client.db1
names=db.project1
# webs=db.web
# animations=db.animation
# hardwares=db.hardware
tracks=db.track
app = Flask(__name__)
api=Api(app)

class project1(Resource):
	def get(self):
		data=[]
		for task in names.find():
			task["_id"]=str(task["_id"])
			data.append(task)
		return data

	def post(self):
		track=request.values.get("track")
		result = names.find({"track":track}).count()
		if(result==0):
			names.insert({"track":track})
			return "added",200
		else:
			return "this track exists"

	def delete(self):
		track=request.values.get("track")
		names.remove({"track":track})
		return "removed",300

	def put(self):
		track=request.values.get("track")
		id=request.values.get("id")
		id =ObjectId(id)	
		names.update({"_id":id}, { "$set":{"track":track}})
		return "updated",400

# class web(Resource):
# 	def get(self):
# 		webdata=[]
# 		for task in webs.find():
# 			task["_id"]=str(task["_id"])
# 			webdata.append(task)
# 		return webdata

# 	def post(self):
# 		projectname=request.values.get("projectname")
# 		result = webs.find({"projectname":projectname}).count()
# 		if(result==0):
# 			webs.insert({"projectname":projectname})
# 			return "added",200
# 		else:
# 			return "this project exists"

# 	def delete(self):
# 		projectname=request.values.get("projectname")
# 		webs.remove({"projectname":projectname})
# 		return "removed",300

# 	def put(self):
# 		projectname=request.values.get("projectname")
# 		id=request.values.get("id")
# 		id =ObjectId(id)	
# 		webs.update({"_id":id}, { "$set":{"projectname":projectname}})
# 		return "updated",400

# class animation(Resource):
# 	def get(self):
# 		anidata=[]
# 		for task in animations.find():
# 			task["_id"]=str(task["_id"])
# 			anidata.append(task)
# 		return anidata

# 	def post(self):
# 		projectname=request.values.get("projectname")
# 		result = animations.find({"projectname":projectname}).count()
# 		if(result==0):
# 			animations.insert({"projectname":projectname})
# 			return "added",200
# 		else:
# 			return "this project exists"

# 	def delete(self):
# 		projectname=request.values.get("projectname")
# 		animations.remove({"projectname":projectname})
# 		return "removed",300

# 	def put(self):
# 		projectname=request.values.get("projectname")
# 		id=request.values.get("id")
# 		id =ObjectId(id)	
# 		animations.update({"_id":id}, { "$set":{"projectname":projectname}})
# 		return "updated",400

# class hardware(Resource):
# 	def get(self):
# 		data=[]
# 		for task in hardwares.find():
# 			task["_id"]=str(task["_id"])
# 			data.append(task)
# 		return data

# 	def post(self):
# 		projectname=request.values.get("projectname")
# 		result = hardwares.find({"projectname":projectname}).count()
# 		if(result==0):
# 			hardwares.insert({"projectname":projectname})
# 			return "added",200
# 		else:
# 			return "this project exists"

# 	def delete(self):
# 		projectname=request.values.get("projectname")
# 		hardwares.remove({"projectname":projectname})
# 		return "removed",300

# 	def put(self):
# 		projectname=request.values.get("projectname")
# 		id=request.values.get("id")
# 		id =ObjectId(id)	
# 		hardwares.update({"_id":id}, { "$set":{"projectname":projectname}})
# 		return "updated",400

class trackk(Resource):
	def get(self):
		trackdata=[]
		trackid=request.values.get("trackid")
		# trackid=ObjectId(trackid)
		# return [str(track['_id']) for track in tracks.find()]
		result=tracks.find({"trackid":trackid}).count()
		print result
		if (result!=0):
			for track in tracks.find({"trackid":trackid}):
				track["_id"]=str(track["_id"])
				trackdata.append(track)
			return trackdata
		else:
			return "no track found"

	def post(self):
		trackid=request.values.get("trackid")
		trackid=str(trackid)
		projectname=request.values.get("projectname")
		result = tracks.find({"projectname":projectname}).count()
		if(result==0):
			tracks.insert({"projectname":projectname, "trackid":trackid})
			return "added",200
		else:
			return "this project exists"

	def delete(self):
		id=request.values.get("trackid")
		trackid=ObjectId(id)
		projectname=request.values.get("projectname")
		result = tracks.find({"projectname":projectname,"trackid":trackid}).count()
		if(result!=0):
			tracks.remove({"projectname":projectname, "trackid":trackid})
			return "removed",300
		else:
			return "this project does not exists"	

	def put(self):
		projectname=request.values.get("projectname")
		trackid=request.values.get("trackid")
		id=request.values.get("id")
		id =ObjectId(id)
		result = tracks.find({"_id":id,"trackid":trackid}).count()
		if (result==0):
			tracks.update({"_id":id}, { "$set":{"projectname":projectname}})
			return "updated",400
		else:
			return "this project does not exists"


# api.add_resource(web,"/web")
# api.add_resource(animation,"/animation")
# api.add_resource(hardware,"/hardware")
api.add_resource(project1,"/")
api.add_resource(trackk,"/track")

if __name__ == "__main__":
	app.run(debug=True)


