from flask import Flask, request
from flasgger import Swagger
import pickle
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
Swagger(app)

pickled_model_file = open("pickle_iris_model.pkl","rb")
classifier = pickle.load(pickled_model_file)

@app.route('/')
def base_route():
    return "Welcome to Pickle code demo"

@app.route("/hello", methods=["GET","POST"])
def hello():
    """Lets try Swagger from flasgger
    ---
    parameters:
        - name: Sepal_width
          in: query
          type: number
          required: true  
        - name: Sepal_length
          in: query
          type: number
          required: true
        - name: Petal_width
          in: query
          type: number
          required: true
        - name: Petal_length
          in: query
          type: number
          required: true
    responses:
        200:
            description: The result is    
    """
    try :
        sw = request.args.get("Sepal_width")
        sl = request.args.get("Sepal_length")
        pw = request.args.get("Petal_width")
        pl = request.args.get("Petal_length")
        #return "Oops something went wrong", 400
        
        result = classifier.predict([[sw,sl,pw,pl]])
        return f"The prediction for flower is {result}"
    except Exception as e :
        return f" Error occuredd with message : {e}", 401

if __name__=="__main__":
    app.run()
