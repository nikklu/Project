def calculus(a,b):
    print(f"the sum of two numbers is: {a+b}")
    if(a>b):
        print(f"{a} is greater than {b}")
        print(f"the difference of two numbers is: {a-b}")

    else:
        print(f"{b} is greater than {a}")   
        print(f"the difference of two numbers is: {b-a}")

    print(f"the product of two numbers is: {a*b}")
    if(b!=0):
        print(f"the division of two numbers is: {int(a/b)}")
    else:
        print("division by zero is not allowed")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
calculus(a,b)
