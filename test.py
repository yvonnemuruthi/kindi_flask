from flask import *

#initializing/ creating flask app
app=Flask(__name__)

#Routing which should start with a slash on quotes"/"
@app.route("/api/home")
def home():
    return jsonify({"message":"Welcome to HOME API"})

@app.route("/api/products")
def products():
    return jsonify({"message":"Welcome to Products API"})

@app.route("/api/about")
def about():
    return jsonify({"message":"More About us API"})

@app.route("/api/sum")
def sum():
    num1=29
    num2=56
    sum=num1+num2
    return jsonify({"Answer":sum})

@app.route("/api/calc",methods=["POST"])
def calc():
    number1=request.form["number1"]
    number2=request.form["number2"]
    sum=int(number1)+int(number2)
    return jsonify({"Answer":sum})

@app.route("/api/multiplication")
def multiplication():
    num1=request.form["num1"]
    num2=request.form["num2"]
    product=int(num1)*int(num2)
    return jsonify({"answer":product})

if __name__=='__main__':
    app.run(debug=True)
