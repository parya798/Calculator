def get_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
             print("please enter a valid number: ")

def calculator():
    print("Welcome")
    while True:
        num1 = get_number("enter the first number: ")
        num2 = get_number("enter the second number: ")
       
        operation = input("enter the operator (+, -, *, /): ")
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("error! division by zero. don't divide numbers by zero please!")
                continue
            result = num1 / num2
        else:
            print("the operator you entered is not valid.")
            continue
        
        print(f"the result: {result}")
        
        play_again = input("do you wanna play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("that's a shame, see you around.")
            break
        
calculator()