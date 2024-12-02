#Print a specific pattern
#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15

num=1
s=2
n=int(input("Enter the number of rows : "))
for i in range(n):
    for j in range(1,s):
        print(num,end=" ")
        num+=1
    print()
    s+=1



