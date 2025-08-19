from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<html><head><title>Demo</title></head><body><h1>Hello World!</h1></body></html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)