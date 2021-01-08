from app import app
from flask import render_template, request
import csv
from app import classes
import sys

@app.route("/")
@app.route("/index")
def index():
    #return "Index page"
    return render_template("base.html")

# @app.route("/index",methods=['POST'])
# def report():
#     return render_template()


# @app.route("/all")
# def all_grades():
#     return ""

@app.route("/class",methods=['GET'])
def find_class():
    return render_template("class.html")

@app.route("/class",methods=['POST'])
def by_class_post():
    class_name = request.form['subject_code'] + ' ' + request.form['course_no']
    cname = class_name.upper()
    year = request.form['year']
    term = request.form['term']
    instructor = request.form['instructor']
    # No options
    if year=="" and term=="" and instructor=="":
        rval = classes.find_class(cname)
        if rval=="Class not found!":
            return render_template("class_error.html",class_name=cname)    
        dist = rval
    # Options
    else:
        rval = classes.find_class_option(cname,year,term,instructor)
        if rval[0] == False:
            if rval[1][0]==False: 
                return render_template("class_error.html",class_name=cname)
            else:
                return render_template("options_error.html",class_name=cname)
        dist = rval[1]
    dist_percent = []
    total = sum(dist)
    for grade in range(len(dist)):
        dist_percent.append((dist[grade]/total))
    avg_gpa = classes.calc_gpa(dist)
    return render_template("distribution2.html",class_name=cname,val=dist_percent,gpa=avg_gpa,year=year,term=term,instructor=instructor)
