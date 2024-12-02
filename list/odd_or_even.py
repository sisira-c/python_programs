a=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    elements=int(input())
    a.append(elements)
odd=[]
even=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(a)
print("list of even numbers are",even)
print("list of odd numbers are",odd)