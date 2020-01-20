from flask import Flask,render_template,redirect,request,session,url_for;
app=Flask(__name__)
app.secret_key="secret"
@app.route("/",methods=['GET','POST'])

def index():
    try:
        balance=session["balance"]
        count=session["count"]
    except KeyError:
        balance = session["balance"]=8000
        count = session["count"]=0

    if request.method=="GET":
         return render_template("index.html",balance=balance,msg=" ",count=count)
    if request.method=="POST":
         if int(request.form["amount"])<0:
             msg="no negative amount"
             return render_template("index.html",balance=balance,msg=msg,count=count)
         if session["count"]>5:
             msg = "exceeded max transaction count"
             return render_template("index.html",balance=balance,msg=msg,count=count)
         if request.form["action"]=="withdraw":
             if int(request.form["amount"])>5000:
                 msg = "more than 5000 amount"
                 return render_template("index.html",balance=balance,msg=msg,count=count)
             else:
                 balance=balance-int(request.form["amount"])
                 session["balance"]=balance
                 session["count"]+=1
                 count=session["count"]
                 msg="withdrawn"
                 return render_template("index.html",balance=balance,msg=msg,count=count)
         else:
             balance = balance + int(request.form["amount"])
             session["balance"] = balance
             session["count"]+=1
             count = session["count"]
             msg = "withdrawn"
             return render_template("index.html", msg=msg, balance=balance, count=count)

if __name__=='__main__':
    app.run(debug=True)

