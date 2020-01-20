from flask import Flask,render_template,redirect,request,session,url_for
app=Flask(__name__)
app.secret_key="secret"
@app.route("/",methods=['GET','POST'])

def index():
     try:
         amount=session["amount"]
     except KeyError:
         amount=session["amount"]=0

     if request.method=='GET':
         return render_template("index.html",msg="welcome")
     if request.method=='POST':
          if request.form["eggs"]=="" or request.form["bread"]=="" or request.form["milk"]=="":
              msg="cannot be empty"
              return render_template("index.html",msg=msg)
          if int(request.form["eggs"])<0 or int(request.form["bread"])<0 or int(request.form["milk"])<0:
              msg="cannot enter negative values"
              return render_template("index.html", msg=msg)

          else:
              amount=(int(request.form["eggs"])*10)+(int(request.form["bread"]) * 20)+(int(request.form["milk"])*30)
              session["amount"]=amount
              msg="added succesfully"
              return render_template("index.html",msg=msg,amount=amount)

if __name__=='__main__':
    app.run(debug=True)