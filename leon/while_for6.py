total1=0
total2=0
count1=0
count2=0
grade = int(input("please enter grade:"))
while 0<grade<100:
    if grade>=60:
        total1+=grade
        count1+=1

    else:
        total2+=grade
        count2+=1
    grade = int(input("please enter grade:"))

print(f"avarge", {total1/count1})
print(f"fail avarge", {total2/count2})

