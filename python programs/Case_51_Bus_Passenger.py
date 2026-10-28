capacity = int(input("Enter bus capacity: "))
passengers = int(input("Enter starting passengers: "))
stops = int(input("Enter number of stops: "))
if capacity < 0 or passengers < 0 or passengers > capacity or stops < 0:
    print("Invalid initial input")
else:
    for i in range(stops):
        getting_off = int(input("Passengers getting off: "))
        getting_on = int(input("Passengers getting on: "))
        if getting_off < 0 or getting_on < 0 or getting_off > passengers:
            print("Invalid passenger counts")
        else:
            passengers = passengers - getting_off + getting_on
            print("Passengers:", passengers)
            if passengers > capacity:
                print("Capacity exceeded")
            else:
                print("Within capacity")

