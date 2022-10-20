print(">" * 5, "Hello", "<" * 5)
one_number = int(input("Enter the first number:"))
two_number = int(input("Enter the second number:"))
action = input("Select an action:")
if action == "+":
    print(one_number+two_number)
elif action == "-":
    print(one_number-two_number)
elif action == "*":
    print(one_number*two_number)
elif action == "/":
    print(one_number/two_number)