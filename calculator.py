print("Pick either addition, subtraction, multiplication, or division:")
opp = input("")
if opp == 'addition':
	num1 = input("Enter your first number:")
	num2 = input("Enter your second number:")
	final = (int(num1) + int(num2))
	print(final)
elif opp == 'subtraction':
	num1 = input("Enter your first number:")
	num2 = input("Enter your second number:")
	final = (int(num1) - int(num2))
	print(final)
elif opp == 'division':
	num1 = input("Enter your first number:")
	num2 = input("Enter your second number:")
	final = (int(num1) / int(num2))
	print(final)
elif opp == 'multiplication':
	num1 = input("Enter your first number:")
	num2 = input("Enter your second number:")
	final = (int(num1) * int(num2))
	print(final)
else:
	print("Sorry, please try again and pick one of the options given.")
