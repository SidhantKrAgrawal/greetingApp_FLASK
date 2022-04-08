from crypt import methods
from enum import Flag

from flask import Flask, flash, render_template, request


from flask import Flask, render_template, request,flash

app=Flask(__name__)
app.secret_key = "a secret"


@app.route("/hello")
def index():
    flash("Whats your name?")
    return render_template("index.html")

@app.route("/greet",methods=['POST','GET'])
def greet():
    flash("Hi "+ str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")
    
if __name__=='__main__':
    app.run(debug=True)