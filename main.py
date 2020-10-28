# This will make the API "work" without us needing to write hundreds of line of code
from flask import Flask, request
from flask_restful import Api, reqparse, Resource, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy # let us save data in a mini local DB rather than in memory

# This line is required to work with Flask. 
app = Flask(__name__)
api = Api(app)

# Configure the local DB to be used and the models (tables) within it
# Where is the database?
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hackathonprototypeforumdb.db'
db = SQLAlchemy(app)

# The messages in the database
class MessageModel(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    body = db.Column(db.String(3000), unique=False, nullable=True)
    views = db.Column(db.Integer, unique=False, nullable=False)
    likes = db.Column(db.Integer, unique=False, nullable=False)
    author = db.Column(db.String(50), unique=False, nullable=False)


# When we retrieve data from the database, describe how to transform(serialise) it into JSON so we can return it to the caller.
message_resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'body': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer,
    'author': fields.String
}

# Once we have defined all the data to save in the database, create it. DO THIS ONCE!
# db.create_all() # This can only run once or it will override all the data in the DB

# This is our prototype 'session' information.
IsLoggedIn = False
username = ""

# For now, store our forum messages in memory
messages={}
users={}
# Define the data format of our message put requests
message_put_args = reqparse.RequestParser()
message_put_args.add_argument("title", type=str, help="Title of the message is required", required=True)
message_put_args.add_argument("body", type=str, help="Body  of the message is required", required=True)
message_put_args.add_argument("views", type=int, help="Views  of the message")
message_put_args.add_argument("likes", type=int, help="likes of the message")

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("user_id", type=int, help="the identifier of the user is required", required=True)
user_put_args.add_argument("name", type=str, help="The name of the user is required", required=True)
user_put_args.add_argument("age", type=int, help="The age of the user is required", required=True)
user_put_args.add_argument("gender", type=str, help="Gender of the user")
user_put_args.add_argument("views", type=int, help="Views  of the user's page")
user_put_args.add_argument("password", type=str, help="You must provide a password")

login_put_args = reqparse.RequestParser()
# In a real system, we would use a user name
login_put_args.add_argument("username", type=str, help="the identifier of the user is required", required=True)
login_put_args.add_argument("password", type=str, help="You must provide a password", required=True)

def get_safe_user_info(id):
    user=users[id]
    safeuser = {"name":user["name"], "views":user["views"], "gender":user["gender"]}
    return (safeuser)

def user_not_logged_in ():
    if not IsLoggedIn:
        abort(401, message="You are not authorised to perfom this operation.")

# Each resource should be declared as a class (an object that will group functions and variables and do something for us)
# It inherits from Resource as that gives us access to API methods to keep development easy.
class Messages(Resource):
    @marshal_with(message_resource_fields) # use this information to turn the data we retrieved into JSON
    def get(self): # Define what happens when Messages receives a "GET" request
        result = MessageModel.query.all()
        return result,200
    @marshal_with(message_resource_fields)
    def post(self): # Define what happens when Messages receives a "POST" request
        user_not_logged_in ()
        args = message_put_args.parse_args()
        message = MessageModel(title=args['title'], body=args['body'], views=0, likes=0, author=username) # The message ID is created automatically by the database.
        db.session.add(message)
        db.session.commit()
        return message, 201 # return added data with Created status code
    
class Message(Resource):
    @marshal_with(message_resource_fields) 
    def get(self, message_id):
        result = MessageModel.query.filter_by(id=message_id).one()
        return result
    def delete(self, message_id):
        # user_not_logged_in ()
        # message_not_found (id)
        # del messages[id]
        return {}, 204
    

class Users(Resource):
    def get(self):
        safeusers={}
        for id in users.keys():
            safeusers[id]=get_safe_user_info(id)
        return safeusers, 200
    def post(self):
        args = user_put_args.parse_args()
        id = args ["user_id"]
        users[id] = args
        return users[id], 201

class Login(Resource):
    def post(self):
        args = login_put_args.parse_args()
        verifyusername = args ["username"]
        global IsLoggedIn
        global username
        if verifyusername.lower() == "soso" and args ["password"] == "1234":
            IsLoggedIn = True
            username = verifyusername
            return {}, 200
        else:
            IsLoggedIn = False
            username = ""
        return {"message": "We can't log you in."}, 401




# class Likes(Resource):
#     def post(self, message_id):
#         user_not_logged_in ()
#         msg=messages[id]
#         likes=msg["likes"]
#         if not likes:
#             likes = 0
#         likes+=1
#         msg["likes"]=likes
#         messages[id] = msg
#         return messages[id], 201
    # def get(self, message_id):
    #     msg=messages[id]
    #     likes=msg["likes"]
    #     return {"likes":likes}, 200


        

# Define the resources that the API knows about and what route (URL) they are found at.
# api.add_resource(Likes, "/messages/<int:message_id>/likes")
api.add_resource(Message, "/messages/<int:message_id>")
api.add_resource(Messages, "/messages")
api.add_resource(Users, "/users")
api.add_resource(Login, "/login")

# Used to start the program when calling python main.py on the command line
if __name__ == "__main__":
    app.run(debug=True) # Remove debug = True for production

