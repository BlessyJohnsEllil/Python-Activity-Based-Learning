basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
overtime = float(input("Enter overtime amount: "))
incentive = float(input("Enter incentive: "))

if basic < 0 or allowance < 0 or overtime < 0 or incentive < 0:
    print("Invalid salary amount")
else:
    gross = basic + allowance + overtime + incentive

    deduction = min(gross, 30000) * 0.05

    if gross > 30000:
        deduction = deduction + min(gross - 30000, 20000) * 0.10

    if gross > 50000:
        deduction = deduction + (gross - 50000) * 0.15

    net_salary = gross - deduction

    print("\n--- SALARY STATEMENT ---")
    print("Gross Salary: Rs.", round(gross, 2))
    print("Total Deduction: Rs.", round(deduction, 2))
    print("Net Salary: Rs.", round(net_salary, 2)) 
