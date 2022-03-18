print ("Welcome to the tip calculator.") 
bill= float(input("What was the total bill?") )
tip = int(input("What percentage would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

tip_percent = bill * (tip/100)
bill_plus_tip = bill + tip_percent
#bill_per_person = round (bill_plus_tip/people, 2)
bill_per_person = "{:.2f}".format(bill_per_person)
print (f"Each person should pay {bill_per_person} Naira")