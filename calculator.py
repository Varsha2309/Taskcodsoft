#ADD TWO NUMBERS
def add(x,y):
    return x + y

#SUBTRACT TWO NUMBERS
def subtract(x,y):
    return x - y

#MULTIPLY TWO NUMBERS
def multiply(x,y):
    return x * y

#DIVIDE TWO NUMBERS
def divide(x,y):
    return x / y

print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    #input from user
    choice = input("Enter choice (1/2/3/4):")

    #check if choice
    if choice in('1','2','3','4'):
        try:
            num1 = float(input("Enter first number :"))
            num2 = float(input("Enter second number :"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
            print(num1, "+",num2,"=",add(num1,num2))

        elif choice == '2':
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice == '3':
            print(num1,"*",num2, "=", multiply(num1,num2))
        elif choice == '4':
            print(num1,"/",num2,"=",divide(num1,num2))

        #check if user wants calculation
        #break while loop
        next_calculation = input("Lets do next calculation? (yes/no):")
        if next_calculation == "no":
          break
    else:
        print("Invalid input")