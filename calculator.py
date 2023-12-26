while True:
    print("\nSelect an operation to perform")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division\n")
    print("Enter q or Q to Exit")
    
    choice=input("Enter your choice:")
    if choice =='q' or choice =='Q':
       break
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))

    if choice=="1":
       print(num1,"+",num2,"=",(num1+num2))
       print("\n")

    elif choice=="2":
       print(num1,"-",num2,"=",(num1-num2))
       print("\n")

    elif choice=="3":
       print(num1,"*",num2,"=",(num1*num2))
       print("\n")

    elif choice=="4":
       if num2==0.0:
          print("Divide by 0 Error")
       else:
          print(num1,"/",num2,"=",(num1/num2))
          print("\n")
          
    else:
        print("Invalid choice")
    
    print()