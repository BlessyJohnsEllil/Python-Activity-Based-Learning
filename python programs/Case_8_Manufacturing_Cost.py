material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
wastage = float(input("Enter wastage cost: "))
machine = float(input("Enter machine cost: "))
selling = float(input("Enter selling price: "))
target = float(input("Enter profit target: "))

total_cost = material + labour + wastage + machine
profit = selling - total_cost

print("Total cost:", total_cost)
print("Profit:", profit)

if profit >= target:
    print("Profit target achieved")
else:
    print("Profit target not achieved")
