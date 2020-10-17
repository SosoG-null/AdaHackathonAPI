# This will make the API "work" without us needing to write hundreds of line of code
from flask import Flask
from flask_restful import Api, reqparse, Resource, abort

# This line is required to work with Flask. 
app = Flask(__name__)
api = Api(app)

# For now, store our forum messages in memory... but not for long!
messages={}
users={}
# Define the data format of our message put requests
message_put_args = reqparse.RequestParser()
message_put_args.add_argument("message_id", type=int, help="the identifier of the message is required", required=True)
message_put_args.add_argument("topic", type=str, help="Topic of the message is required", required=True)
message_put_args.add_argument("body", type=str, help="Body  of the message is required", required=True)
message_put_args.add_argument("author", type=str, help="Author  of the message")
message_put_args.add_argument("views", type=int, help="Views  of the message")
message_put_args.add_argument("likes", type=int, help="likes of the message")

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("user_id", type=int, help="the identifier of the user is required", required=True)
user_put_args.add_argument("name", type=str, help="The name of the user is required", required=True)
user_put_args.add_argument("age", type=str, help="The age of the user is required", required=True)
user_put_args.add_argument("gender", type=str, help="Gender of the user")
user_put_args.add_argument("views", type=int, help="Views  of the user's page")

def message_not_found (id):
    if id not in messages:
        abort(404, message="404:Message ID invalid")
# Each resource should be declared as a class (an object that will group functions and variables and do something for us)
# It inherits from Resource as that gives us access to API methods to keep development easy.
class Messages(Resource):
    def get(self): # Define what happens when Messages receives a "GET" request
        return {"data": messages },200
    def post(self): # Define what happens when Messages receives a "POST" request
        args = message_put_args.parse_args()
        id = args["message_id"]
        # Check if any views were pased in
        views = args["views"]
        if not views:
            views = 0
        likes = args["likes"]
        if not likes:
            likes = 0
        msg = args
        # Save the correct number of views in the message to be stored
        msg["views"] = views
        msg["likes"] = likes
        messages[id] = msg
        return messages[id], 201 # return added data with Created status code
    
    

class Message(Resource):
    def get(self, id):
        message_not_found (id)
        return messages[id], 200
    def delete(self, id):
        message_not_found (id)
        del messages[id]
        return {}, 204
    

class Users(Resource):
    def get(self):
        return {"data":users}, 200
    def post(self):
        args = user_put_args.parse_args()
        id = args ["user_id"]
        users[id] = args
        return users[id], 201

class Likes(Resource):
    def post(self, id):
        msg=messages[id]
        likes=msg["likes"]
        if not likes:
            likes = 0
        likes+=1
        msg["likes"]=likes
        messages[id] = msg
        return messages[id], 201
    def get(self, id):
        msg=messages[id]
        likes=msg["likes"]
        return {"likes":likes}, 200


        

# Define the resources that the API knows about and what route (URL) they are found at.
api.add_resource(Likes, "/messages/<int:id>/likes")
api.add_resource(Message, "/messages/<int:id>")
api.add_resource(Messages, "/messages")
api.add_resource(Users, "/users")

# Used to start the program when calling python main.py on the command line
if __name__ == "__main__":
    app.run(debug=True) # Remove debug = True for production

