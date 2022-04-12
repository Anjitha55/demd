from flask import Flask, request
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/')
def base_route():
    return "Welcome to Praxis"

@app.route("/my_name/<name>")
def print_name(name):
    return f"Welcome to Praxis Happy learning {name} in Nagpur"

@app.route("/hello", methods=["GET","POST"])
def hello():

    """Lets try Swagger from flasgger
    ---
    parameters:
        - name: StudentName
          in: query
          type: string
          required: true  
        - name: RollNo
          in: query
          type: string
          required: true
    responses:
        200:
            description: The result is    
    """
    try :
        stu_name = request.args.get("StudentName")
        numb = request.args.get("RollNo")
        #return "Oops something went wrong", 400
        
        return f"Student name is {stu_name} and roll no is {numb}", 201
    except Exception as e :
        return f" Error occuredd with message : {e}", 401

if __name__=="__main__":
    app.run()
