grade=int(input("enter grade:"))
while grade<0 or grade>100:
    print("invalid grade must be between 0-100")
    grade=int(input("enter grade:"))
if grade>=70:
    print("passed")
else:
    print("failed")
