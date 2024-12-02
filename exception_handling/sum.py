try:
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    sum=num1+num2
    print(f"addition{sum}")
except ValueError:
    print("value is not allowed")
finally:
    print("test finally block")        
