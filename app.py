# Import Flask dependency
from flask import Flask

# Create a new Flask App Instance
app = Flask(__name__)

# Create Flask Routes
@app.route('/')

# Create a function
def hello_world():
    return 'Hello world'