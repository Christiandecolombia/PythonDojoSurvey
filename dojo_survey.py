from flask import Flask,render_template, request, redirect, session,flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
###main page######

@app.route('/')
def index():
    return render_template("dojo_survey.html")

@app.route('/create', methods=['POST']) 
def create():
    
    if len(request.form['name']) < 1:
    	flash("Please enter a name")
    if not '_flashes' in session.keys():	# there are no errors
    	# add user to database
        flash("Ninja successfully added!")

    
    mysql = connectToMySQL("dojo_survey")
    query="insert into ninjas (name,location,language,comments) values(%(name)s, %(location)s,%(language)s,%(comments)s)"
    data={
        "name":request.form["name"],
        "location":request.form['location'],
        "language":request.form['language'],
        "comments":request.form['comments']
     }
    mysql.query_db(query,data)
    session['name']=request.form['name'],
    session['location']=request.form['location'],
    session['language']=request.form['language'],
    session['comments']=request.form['comments']
    return redirect("/result")

###result#######

@app.route('/result')
def result():

    return render_template('result.html')




if __name__ == "__main__":
    app.run(debug=True)

