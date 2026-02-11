from flask import redirect
from flask import Flask,request,render_template

app=Flask(__name__)


@app.route("/",methods=["POST","GET"]    )
@app.route("/home",methods=["POST","GET"])
def homepage():
        returning=""
        if request.method=="POST":
            name=request.form.get("username")
            email=request.form.get("email")
            id=request.form.get("id")
            if name=="admin" and email=="code" and id=="1234":
                return redirect("/verify/"+ name+"/"+id)
            else:
                returning="⚠ Wrong Entry"
                
        return render_template("index.html",returning=returning)

@app.route("/verify/<name>/<id>")
def verifypage(name,id):
    return render_template("success.html",user=name,id=id)

if __name__=="__main__":
    app.run(debug=True)
