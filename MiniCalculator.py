print("---------MINI CALCULATOR---------")
a=int(input("Enter first operand: "))
b=int(input("Enter second operand: "))
choice=input("Enter your choice (+, -, *, /): ")
if choice=='+':
    print("The sum is: ", a+b)  
elif choice=='-':
    print("The difference is: ", a-b)
elif choice=='*':
    print("The product is: ", a*b)
elif choice=='/':
    if b==0:
        print("Math error division by zero is not allowed.")
    else:
        print("The quotient is: ", a/b)
else:
    print("Invalid choice. Please select a valid operation.")

