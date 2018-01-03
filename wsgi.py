from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Goodbye cruel World!"

@application.route("/blackrose/")
def hello2():
    return "This drink sucks"

if __name__ == "__main__":
    application.run()
