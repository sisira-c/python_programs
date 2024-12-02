a=[]
b=[]
a1=int(input("enter the max count of elements in list_1:"))
for i in range(0,a1):
    a2=input(f"enter the element{i+1}in list_1:")
    a.append(a2)
b1=int(input("enter the max count of elements{i+1}in list_2:"))
for i in range(0,b1):
    b2=input(f"enter the element{i+1}in list_2:")
    b.append(b2)
c=[]
for i in a:
    for j in b:
        if i==j:
            c.append(i)
print("common elemets in both the list are:",c)                

