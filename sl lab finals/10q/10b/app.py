from flask import Flask,render_template,redirect,request,session,url_for
import re
import time

app=Flask(__name__)
app.secret_key="secret"
@app.route("/",methods=['GET','POST'])

def index():
    if request.method=="GET":
        return render_template("student.html",msg="")
    if request.method=="POST":
        if request.form["usn"]==" " or request.form["dob"]==" " or request.form['m1']==" " or request.form['m2']==" " or request.form['m3']==" ":
          return render_template("student.html",msg="enter everything")
        if int(request.form['m1'])<0 or int(request.form['m2'])<0 or int(request.form['m3'])<0:
            return render_template("student.html",msg="cmarks can be negative")

        try:
            time.strptime(request.form["dob"],"%d/%m/%Y")

        except ValueError:
            print("invalid dob form")

        if re.match(('^[1][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$'),request.form["usn"]):
           avg=(int(request.form['m1'])+int(request.form['m2'])+int(request.form['m3']))/3
           return render_template("student.html",msg="avg is "+str(avg))
        else:
            return render_template("student.html",msg="invalid usn format")
if __name__=='__main__':
    app.run()