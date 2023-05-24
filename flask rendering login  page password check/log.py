from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def start():
    return render_template("login.html")
@app.route("/welcome")
def welcome():
    return render_template("user.html")

@app.route("/index")
def index():
    lower_letter=False
    upper_letter=False
    num_end=False
    password=request.args.get('password')
    
    lower_letter=any(c.islower()for c in password)
    upper_letter=any(c.isupper()for c in password)
    num_end=password[-1].isdigit()
    report=lower_letter and upper_letter and num_end
    return render_template("thanks.html",report=report,lower=lower_letter,upper=upper_letter,num=num_end)


    
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__=='__main__':
 app.run(debug=True)