from random import randint
num1=randint(1,100)
num2=randint(1,100)
print(num2)
print(num1)
if num1%2==0 and num2%2==0:
    print({num1+num2})
else: print({num1*num2})