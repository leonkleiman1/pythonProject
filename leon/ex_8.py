day=int(input("plese enter day:"))
if 1<=day<=31:
    month=int(input("plese enter month:"))
    if 1<=month<=12:
            year=int(input("plese enter year:"))
            if 1950<=year<=2020:
                y1=year%10
                y2=year//10%10
                print(f"{day}/{month}/{y2}{y1}")
            else:
                print("invalid year")

    else:
        print("invalid month")
else:
    print("invalid day")