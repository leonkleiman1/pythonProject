total=0
count=0
grade=int(input("please enter grade:"))
while 0<grade and grade<100:
    if grade>=60:
        total=total+grade
        count+=1
    print("avarge",total/count)
    grade = int(input("please enter grade:"))