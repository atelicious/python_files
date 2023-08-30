from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "<p>Hello, World</p>"

@app.route('/')
def index():
    return "Index Page"

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        return "POST method received"
    