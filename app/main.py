from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, This is a flask app using github actions'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
