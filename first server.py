from flask import Flask

app = Flask(__name__)
@app.route ("/")
def home():
    return "Hello from my first server!"
@app.route("/hello/<name>")
def hello (name):
    return f"hello, {name} !welcome to my server"
@app.route("/about")
def about():
    return"this server was built by next gen coders."
@app.route("/location")
def location():
    return"nakuru city"
@app.route("/contact")
def contact():
     return"976665666"
@app.route("/activity")
def activity():
    return"coding learning"
@app.route("/age bracket")
def age():
    return"from 9 to 20"
@app.route("/gender")
def gender():
    return"both gender"
@app.route("/next year age")
def nextyearage(age):
    return f"next years intake age bracket will be{6}"
    
if __name__ == '__main__':
    app.run()
