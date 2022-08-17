from random import randint
grade=randint(-100,110)
print(grade)
if 0<=grade<=100:
    if grade>=70:
        print("pass")
    else:print("failed")
else:
    print("error")