# Hackathon forum API project

If you want to edit this API, follow the steps below:

## Software to install

The API will be developed using **Python** with a few libraries to keep it very simple. It can be redeveloped later with other software (.Net Core), but this keeps it nice and easy.

### Visual Studio Code

Our code editor. Download the editor from: https://code.visualstudio.com/

### Python:

Download the software from https://wiki.python.org/moin/BeginnersGuide/Download. Developed using this version: https://www.python.org/downloads/release/python-390/

If you are in a rush and want a quick syntax summary, watch Learn Python in 5 minutes: https://www.youtube.com/watch?v=I2wURDqiXdM

**Important**: Tick the box to add Python to the PATH.

### Requirements for the project

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
Save the list above as __requirements.txt__ on your hard disk 

Open a command prompt (cmd) and type __pip__ then hit __ENTER__. You should see a list of commands. If you do, you are ready to begin.

- To install all the requirements, type __pip install -r requirements.txt__



## The API routes and resources

### Users

The route to maintain the list of users.

End point: __base address + /users__

Methods:

- Get: Return a list of users without sensitive information
- Post: Create a new user
- TODO: More methods for admins, ...

### Users

The route to maintain the list of users and apply actions like adding likes, comments (to do), ...

End points: 
- __base address + /messages/__
- __base address + /messages/[id]__
- __base address + /messages/[id]/likes__

Methods:

- Get: get a single message or the list of all messages
- Post: Add a message, add a like for a message...
- Delete: Remove a message
- TODO: Comment on message, handle views...

### Login (authentication)

The route to authenticate a user.

End point: __base address + /login__

Methods:

- Post: Check user name and password
- TODO: Sign up, sign out, actually check password, ...
