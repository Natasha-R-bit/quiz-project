
from flask import Flask,render_template,request,session

app = Flask(__name__)
app.config["SECRET_KEY"]="1234"

@app.route("/")
def hello_world():
    name="natasha"
    session["myname"]=name
    session.clear()
    return render_template("index.html")

@app.route("/abouttheauthor")
def about_me():
    return render_template("abouttheauthor.html")

@app.route("/history")
def cities():
    return render_template("history.html")
    
@app.route("/login")
def login():
    return render_template("loginpage.html")



@app.route('/evenorodd')
def evenorodd():
    return render_template('evenorodd.html')

@app.route('/validateevenorodd')
def validateevenorodd():
    number = int(request.args.get('number'))

    result=''
    if number%2==0:
        result="even number"
    else:
        result="odd number"

    return render_template('evenorodd.html',result=result)

@app.route('/greatestnum')
def greatestnum():
    return render_template('greatestnum.html')

@app.route('/validategreatestnum', methods=["post"])
def validategreatestnum():
    num1 = int(request.form.get('num1'))
    num2 = int(request.form.get('num2'))
    num3 = int(request.form.get('num3'))

    result=''
    if num1>num2 and num1>num3:
        result="The first number is the greatest number."
    if num2>num1 and num2>num3:
        result="The second number is the greatest number."
    if num3>num1 and num3>num2:
        result="The third number is the greatest number."
    return render_template("greatestnum.html",result=result)
#logic for all questions
def validate_questions(user_action,correct_answer):
    score=session.get("user_score",0)
    if user_action==correct_answer:
        result="Congratulations! Your answer is correct."
        score=score+10
    else:
        result="Try Again!"
    session["user_score"]=score
    output=[result,score]
    return output

@app.route('/q1',methods=["GET","POST"])
def q1():
    if request.method=="GET":
        return render_template("gq1.html",result="")
    else:
        user_option = request.form.get('q1')
        correct_answer = "c"
        result=validate_questions(user_option,correct_answer)
        print(result)
        return render_template("gq1.html", result=result)

@app.route ('/q2',methods=["GET","POST"])
def q2():
    if request.method=="GET":
        return render_template("gq2.html",result="")
    else:
        user_action=request.form.get("q2")
        correct_answer="a"
        result=validate_questions(user_action,correct_answer)
        return render_template("gq2.html", result=result)

@app.route ('/q3',methods=["GET","POST"])
def q3():
    if request.method=="GET":
        return render_template("gq3.html",result="")
    else:
        user_action=request.form.get("q3")
        correct_answer="b"
        result=validate_questions(user_action,correct_answer)
        return render_template("gq3.html", result=result) 

@app.route ('/q4',methods=["GET","POST"])
def q4():
    if request.method=="GET":
        return render_template("gq4.html",result="")
    else:
        user_action=request.form.get("q4")
        correct_answer="c"
        result=validate_questions(user_action,correct_answer)
        return render_template("gq4.html", result=result) 

@app.route ('/q5',methods=["GET","POST"])
def q5():
    if request.method=="GET":
        return render_template("gq5.html",result="")
    else:
        user_action=request.form.get("q5")
        correct_answer="b"
        result=validate_questions(user_action,correct_answer)
        return render_template("gq5.html", result=result) 

@app.route ('/q6',methods=["GET","POST"])
def q6():
    if request.method=="GET":
        return render_template("gq6.html",result="")
    else:
        user_action=request.form.get("q6")
        correct_answer="b"
        result=validate_questions(user_action,correct_answer)
        return render_template("gq6.html", result=result)

@app.route ('/q7',methods=["GET","POST"])
def q7():
    if request.method=="GET":
        return render_template("gq7.html",result="")
    else:
        user_action=request.form.get("q7")
        correct_answer="a"
        result=validate_questions(user_action,correct_answer)
        return render_template("gq7.html", result=result) 

@app.route ('/q8',methods=["GET","POST"])
def q8():
    if request.method=="GET":
        return render_template("gq8.html",result="")
    else:
        user_action=request.form.get("q8")
        correct_answer="a"
        result=validate_questions(user_action,correct_answer)
        return render_template("gq8.html", result=result) 

@app.route ('/q9',methods=["GET","POST"])
def q9():
    if request.method=="GET":
        return render_template("gq9.html",result="")
    else:
        user_action=request.form.get("q9")
        correct_answer="a"
        result=validate_questions(user_action,correct_answer)
        return render_template("gq9.html", result=result)

@app.route ('/q10',methods=["GET","POST"])
def q10():
    if request.method=="GET":
        return render_template("gq10.html",result="")
    else:
        user_action=request.form.get("q10")
        correct_answer="c"
        result=validate_questions(user_action,correct_answer)
        return render_template("gq10.html", result=result) 
 




@app.route ('/shippingcost' , methods=["GET","POST"])
def shippingcost():
    if request.method=="GET":
        return render_template("shippingcost.html")
    else:
        weight=float(request.form.get("shippingcost"))
        if weight<=20:
            if weight==20:
                result="The cost is $10 per KG."
            elif weight>=10 and weight<20:
                result="The cost is $12 per KG."
            elif weight>=1 and weight<10:
                result="The cost is $14 per KG."
            elif weight<1:
                result="The cost is Free!"
        else:
            result="Your package cannot be delivered."
    return render_template("shippingcost.html", result=result)

@app.route ('/certificate', methods=["GET","POST"])
def certificate():
    if request.method=="GET":
        return render_template("certificate.html")
    if request.method=="POST":
        name=request.form.get("username")
        return render_template("certificate.html",name=name)



if __name__=="__main__":
    app.run(debug=True)  

