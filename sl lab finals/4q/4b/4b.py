from flask import Flask,request,render_template,redirect,session,url_for
app=Flask(__name__)
app.secret_key="secret"
@app.route("/",methods=['GET','POST'])

def store():
    if request.method=="GET":
        return render_template("store.html")
    if request.method=="POST":
        for item in ["eggs","bread","biscuit"]:
            if item not in session:
                session[item]=int(request.form[item])
            else:
                session[item] += int(request.form[item])
        return redirect(url_for("cart"))

@app.route("/cart",methods=['GET','POST'])

def cart():
    cart=[]
    for item in ["eggs","bread","biscuit"]:
        cart.append({"name":item.capitalize(),"quantity":session[item]})
    return render_template("cart.html",cart=cart)

if __name__=='__main__':
    app.run()

