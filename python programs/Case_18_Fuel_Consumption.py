distance = float(input("Enter journey distance: "))
fuel_price = float(input("Enter fuel price per litre: "))
reserve = float(input("Enter reserve percentage: "))

mileage1 = float(input("Enter mileage of Vehicle 1: "))
mileage2 = float(input("Enter mileage of Vehicle 2: "))
mileage3 = float(input("Enter mileage of Vehicle 3: "))

if distance < 0 or fuel_price < 0 or reserve < 0 or mileage1 <= 0 or mileage2 <= 0 or mileage3 <= 0:
    print("Invalid input")
else:
    fuel1 = distance / mileage1
    fuel2 = distance / mileage2
    fuel3 = distance / mileage3

    fuel1 = fuel1 + (fuel1 * reserve / 100)
    fuel2 = fuel2 + (fuel2 * reserve / 100)
    fuel3 = fuel3 + (fuel3 * reserve / 100)

    cost1 = fuel1 * fuel_price
    cost2 = fuel2 * fuel_price
    cost3 = fuel3 * fuel_price

    print("Vehicle 1 fuel with reserve:", fuel1)
    print("Vehicle 1 cost:", cost1)

    print("Vehicle 2 fuel with reserve:", fuel2)
    print("Vehicle 2 cost:", cost2)

    print("Vehicle 3 fuel with reserve:", fuel3)
    print("Vehicle 3 cost:", cost3)

    if cost1 <= cost2 and cost1 <= cost3:
        print("Vehicle 1 is the cheapest")
    elif cost2 <= cost1 and cost2 <= cost3:
        print("Vehicle 2 is the cheapest")
    else:
        print("Vehicle 3 is the cheapest")
