num1=int(input("please enter num:"))
num2=int(input("please enter num:"))

while num1%2==0 and num2%2==0:
    print(num1+num2)
    num1 = int(input("please enter num:"))
    num2 = int(input("please enter num:"))
else:
    print(num1*num2)
