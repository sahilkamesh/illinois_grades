import csv

num_total = {}
num_four = {}

with open('uiuc-gpa-dataset-2015-2020.csv',newline='') as csvfile:
    reader = csv.reader(csvfile)
    i = 0
    for row in reader:
        i+=1
        if i==1:
            continue
        if i==100:
            break
        # if i < 10:
        #     print(row)
        curr_class = row[3]+' '+row[4]
        total = 0
        four = 0
        for grade in row[6:8]:
            total+=int(grade)
            four+=int(grade)
        for grade in row[8:20]:
            total+=int(grade)
            num_total[curr_class] = num_total.get(curr_class,0) + total
            num_four[curr_class] = num_four.get(curr_class,0) + four

print(num_four)
print(num_total)

# for curr_class in num_total.keys():
#     print(curr_class,": ",(num_four[curr_class]/num_total[curr_class])*100,"%")

