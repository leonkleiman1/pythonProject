num=int(input("plese enter 3 difit number:"))

while 100<=num<=999:
    m=int(num//10%10)
    l=int(num//100)
    r=int(num%10)
    print(m+l+r)
    num=int(input("plese enter 3 difit number:"))
print("failed")