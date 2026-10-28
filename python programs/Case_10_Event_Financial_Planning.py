import math
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost: "))
sponsorship = float(input("Enter sponsorship amount: "))
registration_fee = float(input("Enter registration fee per person: "))
total_cost = venue + equipment + catering + transport + certificate
remaining = total_cost - sponsorship
print("Total event cost:", total_cost)
print("Amount after sponsorship:", remaining)
if registration_fee <= 0:
    print("Registration fee must be greater than zero")
else:
    if remaining <= 0:
        registrations = 0
    else:
        registrations = math.ceil(remaining / registration_fee)
    print("Minimum registrations required:", registrations)