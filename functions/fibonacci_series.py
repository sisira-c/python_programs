def fib(i):
    if i<=1:
        return i
    else:
        return(fib(i-1)+fib(i-2))
    
    if num<=0:
       print("please enter a positive number")
    else:
       print("fibonacci series:",end=" ")
    for i in range(num):
       print(fib(i))  
num=int(input("enter the limit:"))
fib(num)  