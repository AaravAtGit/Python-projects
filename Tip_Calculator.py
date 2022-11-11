print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill: "))
tip = float(input("how much tip whould you like to give in percentage: "))
split = int(input("how many people to split the bill: "))

tips = tip / 100
actual_tip = 1 + tips

each_person = (total_bill / split) * actual_tip

rounded = round(each_person, 2)
print(f"Each person should pay: {rounded}")
