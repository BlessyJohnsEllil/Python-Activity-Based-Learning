attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))
required = float(input("Enter required attendance percentage: "))

if (total <= 0 or attended < 0 or attended > total
        or required < 0 or required > 100):
    print("Invalid input")
else:
    percentage = attended / total * 100
    print("Current attendance:", round(percentage, 2), "%")
    
    if percentage >= required:
        print("Required attendance is already achieved")
    elif required == 100 and percentage < 100:
        print("100% attendance cannot be reached under either scenario")
    else:
        # Scenario A: Attend every future class
        a_attended = attended
        a_total = total
        a_classes = 0
        while (a_attended / a_total * 100 < required) and (a_classes < 10000):
            a_attended = a_attended + 1
            a_total = a_total + 1
            a_classes = a_classes + 1
            
        print("\nScenario A: Attend every class")
        if a_classes >= 10000:
            print("Target not reached within limit")
        else:
            print("Classes required:", a_classes)
            print("Final attendance:", round(a_attended / a_total * 100, 2), "%")
            
        # Scenario B: Attend 4 out of every 5 classes
        b_attended = attended
        b_total = total
        b_classes = 0
        while (b_attended / b_total * 100 < required) and (b_classes < 10000):
            b_classes = b_classes + 1
            if b_classes % 5 != 0:
                b_attended = b_attended + 1
            b_total = b_total + 1
            
        print("\nScenario B: Attend 4 out of every 5 classes")
        if b_classes >= 10000:
            print("Target not reached within limit")
        else:
            print("Classes required:", b_classes)
            print("Final attendance:", round(b_attended / b_total * 100, 2), "%")