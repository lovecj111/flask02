from flask import Flask
from api.urls import bp

app = Flask(__name__)
app.register_blueprint(bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()