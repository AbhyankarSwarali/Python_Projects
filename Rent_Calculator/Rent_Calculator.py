rent = int(input("Enter monthly rent: "))
food = int(input("Enter food_bill: "))
elec = int(input("Enter total electricity units spent: "))
elec_charge_amt = 6.5
person = int(input("Enter number of people living:"))

elec_bill = elec * elec_charge_amt

Bill = (food + elec_bill + rent) / person

print("Money spent per person: ", Bill)