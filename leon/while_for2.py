count=0
total=0
for i in range(6):
    num = int(input(f"enter num {i + 1}:"))
    if num%2!=0:
        continue
    total+=num%2==0
    count+=1
print("total",total)
print("average",total/count)


