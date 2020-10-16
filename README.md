# Hackathon forum API project

## Pre-development steps

- Review your design
- Watch the first 6 minutes of this video and decide what the "resources" in our project will be: https://www.youtube.com/watch?v=4T5Gnrmzjak

## Software to install

The API will be developed using **Python** with a few libraries to keep it very simple. It can be redeveloped later with other software (.Net Core), but this keeps it nice and easy.

### Visual Studio Code

Our code editor. Download the editor from: https://code.visualstudio.com/

### Python:

Download the software from https://wiki.python.org/moin/BeginnersGuide/Download. Developed using this version: https://www.python.org/downloads/release/python-390/

If you are in a rush and want a quick syntax summary, watch Learn Python in 5 minutes: https://www.youtube.com/watch?v=I2wURDqiXdM

**Important**: Tick the box to add Python to the PATH.

### Requirements for the project

To make it easier to create an API in Python, we will be installing the following libraries. Don't worry about what's in them. They are here to help:

```aniso8601==8.0.0
click==7.1.2
Flask==1.1.2
Flask-RESTful==0.3.8
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
pytz==2020.1
six==1.15.0
SQLAlchemy==1.3.18
Werkzeug==1.0.1
requests==2.24.0
```
Save the list above as __requirements.txt__ on your hard disk (maybe in your Python projects folder)

Open a command prompt (cmd) and type __pip__ then hit __ENTER__. You should see a list of commands. If you do, you are ready to begin.

- To install all the requirements, type __pip install -r requirements.txt__

### Before we dive into it: Hello world!

- Create a file in your project directory called: **main.py**
- Put the following command in it: print("Hello World")
- Save it
- Then, from the __Command Prompt__ or __Visual Code Terminal__ type python main.py
- If you see Hello World printed under the command, we are ready!

Now let's write some real code in our API...

## The API routes and resources

TODO: SOLANGE. For example:

### List all topics

**Definition**

`GET /topics`

**Response**

List the result you expect for each type of command on each reosurce. Can be done elsehwere.

- `200 OK` on success

```json
[
    {
        "title": "A topic title",
        "startedBy": "Jane Doe"
    },
    {
        "title": "Another topic",
        "startedBy": "John Smith"
    }
]
```

## The main.py file

Create a main.py file and copy and past the following commands into it. This is the base template for our API. It does not do much, but it's a start.

--- Start after this line ---
```
# This will make the API "work" without us needing to write hundreds of line of code
from flask import Flask
from flask_restful import Api, Resource

# This line is required to work with Flask. 
app = Flask(__name__)
api = Api(app)

# Here is a sample API "resource" for testing. Remove it once you write the real code
# Each resource should be declared as a class (an object that will group functions and variables and do something for us)
# It inherits from Resource as that gives us access to API methods to keep development easy.
class HelloWorld(Resource):
    def get(self): # Define what happens when HelloWorld receives a "GET" request
        return {"data": "Hello World!"}

# Define the resources that the API knows about and what route (URL) they are found at. Add your own here.
api.add_resource(HelloWorld, "/helloworld")

# Used to start the program when calling python main.py on the command line
if __name__ == "__main__":
    app.run(debug=True) # Remove debug = True for production
```
--- End before this line ---

## The test.py file

This is where you can run tests without needing a browser. Create a **test.py** file and put the following code in there to test Hello World. We can add to it as we develop.

```# This lets us try out our methods without needing another tool or having to go to the browser every time.
# It is not required. 
# To test it:
# - Go to the directory where your project files are saved
# - Run python main.py in one command line window
# - Run python test.py in a separate command line window. 
# If everything works, you should see the results of your call appear.
# Or try the address below + resource name in your browser.
import requests

BASE = "http://127.0.0.1:5000/" # This is the address that is shown when we run main.py

# Test HellowWorld
response = requests.get(BASE + "helloworld")
print(response.status_code)
print(response.json())
```

You should see a result like so:

```G:\SoftwareDev\Projects\Python\ForumAPITest>python test.py
200
{'data': 'Hello World!'}
```