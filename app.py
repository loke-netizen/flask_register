from flask import request
from flask import render_template
from flask import Flask
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def homepage():
    return render_template("index.html")
@app.route("/verify",methods=["POST"])
def verifypage():
    name=request.form.get("username")
    email=request.form.get("email")
    id=request.form.get("id")
    return render_template("success.html",user=name,mail=email,password=id)
if __name__=="__main__":
    app.run(debug=True)
