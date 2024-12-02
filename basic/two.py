#Print a right pyramid using * and +
# *
# * +
# * + *
# * + * +
# * + * + *
# * + * +
# * + *
# * +
# *

# Printing the first part of the pattern (increasing)
n=int(input("Enter the number : "))
for i in range(1, n):
    for j in range(i):
        if j % 2 == 0:
            print("*", end=" ")
        else:
            print("+", end=" ")
    print()

# Printing the second part of the pattern (decreasing)
for i in range(n-2, 0, -1):
    for j in range(i):
        if j % 2 == 0:
            print("*", end=" ")
        else:
            print("+", end=" ")
    print()
