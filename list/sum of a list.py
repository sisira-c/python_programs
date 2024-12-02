limit=int(input("enter thenumber of elements:"))
a=[]
b=[]
sum=[]
for i in range(0,limit):
  a1=int(input("enter the first list:"))
  a.append(a1)
for i in range(0,limit):
  b1=int(input("enter the second list:"))
  b.append(b1)
print("first list",a)
print("second list",b)
for j in range(0,limit):
  sum1=a[j]+b[j]
  sum.append(sum1)
print(sum)
