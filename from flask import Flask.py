from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "hello from my first server!"

@app.route("/")
def hello(name):
    return f"hello,{name}! welcome to my server."

@app.route("/next/<int:age>")
def next_year(age):
    return f"Next year you will be age{age+1}"

from flask import Flask,jsonify
import random

facts= ["Fact one.","Fact two","Fact three"]
@app.route ("/api/fact/random/")
def fact ():
    return jsonify({"fact":random.choice(facts)})

@app.route("/api/fact/<int:n>")
def fact_n(n):
    if n < len(facts):
        return jsonify({"fact":facts[n]})
    else:
        return jsonify({"error":"No such fact"}),404

if __name__=="__main__":
    app.run(debug=True)
