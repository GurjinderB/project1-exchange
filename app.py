from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_internet():
    return 'Hello Internet!'

@app.route('/<int:i>')
def square(i):
    return str(i**2)

@app.route('/<name>')
def greeting(name):
    return f'hello {name}'

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)