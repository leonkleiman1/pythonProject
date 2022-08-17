num=int(input("please enter num:"))
count=0
while num!=0:
    if num%7==0 or num%3==0:
     count+=1
     num=int(input("please enter num:"))

    print(count)
