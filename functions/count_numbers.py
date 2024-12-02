def count_numbers(n):
    count=0
    while n!=0:
        count+=1
        n//=10
    print(count)
n=int(input("enter the numbers:"))
count_numbers(n)   