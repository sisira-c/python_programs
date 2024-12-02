a=[]
n=int(input("enter the max limit of the list:"))
for i in range(0,n):
    num=input(f"enter the element{i+1}:")
    a.append(num)
print("main list",a)
print("reversed list:",a[::-1])       


   