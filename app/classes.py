import csv
import numpy as np

class_dict = {}

def find_class(cname):
    if class_dict=={}:
        init_classes()  
    if cname in class_dict.keys():
        return class_dict[cname]
    else:
        return "Class not found!"

def find_class_option(cname,year,term,instructor):
    class_check=year_check=term_check=instructor_check=False
    if year=="":
        year_check=True
    if term=="":
        term_check=True
    if instructor=="":
        instructor_check=True
    if class_dict!={}:
        if cname not in class_dict.keys():
            return [False,[class_check,year_check,term_check,instructor_check]]
        class_check=True
    curr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    check = False
    with open("D:\\Desktop\\UIUC\\Class Grades Project\\illinois_grades\\app\\uiuc-gpa-dataset.csv",newline='') as csvfile:
        reader = csv.reader(csvfile)
        first = True
        for row in reader:
            if first:
                first = False
                continue
            curr_class = row[3]+' '+row[4]
            if curr_class!=cname:
                continue
            else:
                class_check=True
            if year!="":
                if row[0]!=year:
                    continue
                else:
                    year_check=True
            if term!="":
                if row[1]!=term:
                    continue
                else:
                    term_check=True
            if instructor!="":
                if row[-2]!=instructor:
                    continue
                else:
                    instructor_check=True
            curr_grades = row[6:20]
            curr_grades = list(map(int, curr_grades))
            curr = np.add(curr,curr_grades)
            check = True
    if check==False:
        return [False,[class_check,year_check,term_check,instructor_check]]
    else:
        return [True,curr]
        

def calc_gpa(grades):
    summing = (grades[0]*4.00+grades[1]*4.00+grades[2]*3.67+grades[3]*3.33+grades[4]*3.00+grades[5]*2.67
                +grades[6]*2.33+grades[7]*2.00+grades[8]*1.67+grades[9]*1.33+grades[10]*1.00+grades[11]*0.67
                +grades[12]*0.00)
    total = sum(grades[:-1])
    avg = summing/total
    return round(avg, 2)

def init_classes():    
    with open("D:\\Desktop\\UIUC\\Class Grades Project\\illinois_grades\\app\\uiuc-gpa-dataset.csv",newline='') as csvfile:
        reader = csv.reader(csvfile)
        first = True
        for row in reader:
            if first:
                first = False
                continue
            curr_class = row[3]+' '+row[4]
            curr_grades = row[6:20]
            curr_grades = list(map(int, curr_grades))
            if curr_class not in class_dict:
                class_dict[curr_class] = curr_grades
            else:
                class_dict[curr_class] = np.add(class_dict[curr_class],curr_grades)
