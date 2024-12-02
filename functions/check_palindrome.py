def is_palindrome(s):
    if s==s[::-1]:
        print("palindrome")
    else:
        print("not palindrome")
    return s
n=input("enter the string:") 
print(is_palindrome(n))       