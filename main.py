# This will make the API "work" without us needing to write hundreds of line of code
from flask import Flask
from flask_restful import Api, reqparse, Resource

# This line is required to work with Flask. 
app = Flask(__name__)
api = Api(app)

messages={}

# Define the data format of our message put requests
message_put_args = reqparse.RequestParser()
message_put_args.add_argument("message_id", type=int, help="the identifier of the message is required", required=True)
message_put_args.add_argument("topic", type=str, help="Topic of the message is required", required=True)
message_put_args.add_argument("body", type=str, help="Body  of the message is required", required=True)
message_put_args.add_argument("author", type=str, help="Author  of the message")
message_put_args.add_argument("views", type=int, help="Views  of the message")

# Each resource should be declared as a class (an object that will group functions and variables and do something for us)
# It inherits from Resource as that gives us access to API methods to keep development easy.
class Messages(Resource):
    def get(self): # Define what happens when HelloWorld receives a "GET" request
        return {"data": messages },200
    def post(self):
        args = message_put_args.parse_args()
        id = args["message_id"]
        # abort_if_message_id_exists(id)
        messages[id] = args
        return messages[id], 201 # return added data with Created status code

        

# Define the resources that the API knows about and what route (URL) they are found at. Add your own here.
api.add_resource(Messages, "/messages")

# Used to start the program when calling python main.py on the command line
if __name__ == "__main__":
    app.run(debug=True) # Remove debug = True for production

