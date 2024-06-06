rent= int(input("Enter your rent of this month:"))
food = int(input("Enter the amount food ordered:"))
electricity = int(input("Enter the total of electricity spend:"))
charge_per_unit = int(input("Enter the charge per unit:"))
person = int(input("Enter the total no of persons living in room:"))

total_electricity_bill = electricity * charge_per_unit

output = (food + rent + total_electricity_bill) // person

print("Each person will pay:", output)