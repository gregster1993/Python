print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100 * bill + bill
total_bill = tip_as_percent / people
final_amount = round(total_bill, 2)
print(f"Each person should pay: ${final_amount}")
# tip_percentage = tip / 100
# bill_with_tip = bill * tip_percentage
# total_bill_with_tip = bill + bill_with_tip
# total_amount = total_bill_with_tip / people
# round_amount = round(total_amount, 2)
# print(f"Each person should pay: ${round_amount}")