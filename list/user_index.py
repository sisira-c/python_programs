l1=[]
n=int(input("enter the limit:"))
for i in range(0,n):
    k=int(input())
    l1.append(k)
c=0
e=int(input("enter the number"))
for i in l1:
  if i==e:
   a=l1[i]-1
print(e,"occured in",a,"th index")