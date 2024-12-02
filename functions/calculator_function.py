def calculator(c,a,b):
    if c==1:
        result=a+b
    elif c==2:
        result=a-b
    elif c==3:
        result=a*b
    elif c==4:
        result=a/b
    else:
        print("invalid")
    return result
    
    
choice=int(input("enter your choice"))
n1=int(input("enter first number"))
n2=int(input("enter second number"))
print(calculator(choice,n1,n2))
                    
   
