from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def base_route():
    return "Welcome to Praxis-demd midterm"

@app.route("/<name>")
def print_welcome_msg(name):
    return f"welcome {name}"

if __name__=="__main__":
    app.run(port = 8080)
