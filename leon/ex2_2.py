num=int(input("enter numer:"))
if 99<num<=999:
    num_r=num//100
    num_l=num%10
    num_m=num//10%10
    y={num_l+num_r+num_m}
    print(y)
else:print("error")