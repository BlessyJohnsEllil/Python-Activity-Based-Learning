products = int(input("Enter number of products: "))
threshold = float(input("Enter fluctuation threshold: "))

if products < 0 or threshold < 0:
    print("Invalid input")
else:
    names = []
    old_prices = []
    new_prices = []
    changes = []

    for i in range(products):
        name = input("Enter product name: ")
        old_price = float(input("Enter old price: "))
        new_price = float(input("Enter new price: "))

        names.append(name)
        old_prices.append(old_price)
        new_prices.append(new_price)

        if old_price <= 0 or new_price < 0:
            print("Invalid price")
            changes.append(-1)
        else:
            percentage = abs(new_price - old_price) / old_price * 100
            changes.append(percentage)

            print("Percentage change:", percentage, "%")

            if percentage > threshold:
                print("Fluctuation is high")

    valid_changes = [x for x in changes if x >= 0]

    if len(valid_changes) == 0:
        print("No valid prices were entered")
    else:
        largest = max(valid_changes)
        position = changes.index(largest)

        print("Largest fluctuation:", largest, "%")
        print("Product:", names[position])
