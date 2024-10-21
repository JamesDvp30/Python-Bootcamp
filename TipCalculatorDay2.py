print("Welcome to the tip calculator!")

bill = float(input(" what is the total bill?"))

tip = int(input("how much tip would you like to give? 10, 12, or 15?"))

subtotal = bill + (bill * (tip / 100)) 

people = int(input("how many people to split the bill?"))

total = round(((subtotal)/ people),2)


print(f"Each person should pay: {total}")




