#  PROJECT (TIP CALCULATOR)
print("WELCOME TO TIP CALCULATOR")
Bill = float(input("What was the total bill? $"))
perc_tip = int(input("How much tip would you like to give? 10,12, or 15?"))
people = int(input("How many people to split the bill?"))
tip_as_percent = perc_tip / 100
total_tip_amount = Bill * tip_as_percent
total_bill = Bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


print(f"Each person should pay : ${final_amount}")