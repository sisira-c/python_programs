l1=[]
pl=[]
npl=[]
n=int(input("enter the limit:"))
for i in range(0,n):
    k=int(input("enter the number of elements:"))
    l1.append(k)
 
for i in range(0,n):
    if l1[i]==1:
        continue
    for j in range(2,l1[i]):
        if l1[i]%j==0:
            npl.append(l1[i])
            break
    else:
            pl.append(l1[i])
print("prime list",pl)            
                    