capacity = float(input("Enter tank capacity: "))
level = float(input("Enter starting water level: "))
days = int(input("Enter number of days: "))
threshold = float(input("Enter required threshold: "))

if capacity <= 0 or level < 0 or level > capacity or days < 0 or threshold < 0 or threshold > capacity:
    print("Invalid input")
else:
    first_interval = 0

    for i in range(days):
        inflow = float(input("Enter water inflow: "))
        outflow = float(input("Enter water outflow: "))

        if inflow < 0 or outflow < 0:
            print("Invalid inflow or outflow")
        else:
            level = level + inflow - outflow

            if level > capacity:
                print("Overflow")
                level = capacity
            elif level < 0:
                print("Shortage")
                level = 0

            print("Water level:", level)

            if level >= threshold:
                print("Threshold reached")
                if first_interval == 0:
                    first_interval = i + 1
            else:
                print("Below threshold")

    if first_interval == 0:
        print("Threshold was not reached")
    else:
        print("First interval reaching threshold:", first_interval)
