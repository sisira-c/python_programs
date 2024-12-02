try:
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    result=num1/num2
    print(f"division{result}")
except ZeroDivisionError:
    print("division by zero is not allowed")
except ValueError:
    print("invalid input") 
finally:
    print("test finally block")         