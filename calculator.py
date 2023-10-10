#Basic calculator using Python

#Taking input values
print("This is your basic calculator")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

#For performing operations
op=0
while op<7:
    print('Operations to perform: ')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Modulus')
    print('6. Exponential')
    op = int(input("Enter your choice: "))

    #conditions
    if op==1:
        c=a+b
        print("Sum: ", c)
    elif op==2:
        c=a-b
        print("Difference: ",c)
    elif op==3:
        c=a*b
        print("Product: ",c)
    elif op==4:
        c=a/b
        print("Quotient: ",c)
    elif op==5:
        c=a%b
        print("Modulud: ",c)
    elif op==6:
        c=a^b
        print("Exponent value: ",c)
    elif op==7:
        break
    else:
        print("Please enter the valid choice!")
