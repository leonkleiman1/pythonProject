
num1=int(input("plese enter num:"))
print(num1)
while 10<=num1<=99:
    if num1%7==0 or num1%10 == 7 or num1//10 == 7:
        print("lucky number")
    else:
        print("not lucky number")
    num1 = int(input("plese enter num:"))
    print(num1)
else:
    print("error")
