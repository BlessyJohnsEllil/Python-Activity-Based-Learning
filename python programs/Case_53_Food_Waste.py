days = int(input("Enter number of days: "))
limit = float(input("Enter wastage limit percentage: "))
if days < 0 or limit < 0 or limit > 100:
    print("Invalid input")
else:
    for i in range(days):
        prepared = int(input("Enter meals prepared: "))
        served = int(input("Enter meals served: "))
        leftover = int(input("Enter leftover meals: "))
        if prepared <= 0 or served < 0 or leftover < 0 or served + leftover > prepared:
            print("Invalid meal counts")
        else:
            wastage = leftover / prepared * 100
            print("Wastage percentage:", wastage, "%")
            if wastage > limit:
                print("Wastage limit exceeded")
            else:
                print("Wastage is within limit")
