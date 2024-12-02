a=[]
n=int(input("enter the limit"))
for i in range(1,n+1):
    k=int(input("numbers"))
    a.append(k)
big=a[0]
for i in range(1,n):
    if a[i]>big:
        big=a[i]
print("largest element in a last",big)
i=0 
while(i):
  if a[i]!=big:
    sbig=a[i]
    break
  i+=1
for i in range(i+1,n):
  if a[i]<big and a[i]>sbig: 
      sbig=a[i]
print("second largest",sbig)                          