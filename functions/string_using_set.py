# def vowel_count(str):
#    count=0
#    vowel=set("aeiouAEIOU")
#    for alphabet in str:
#         if alphabet in vowel:
#             count=count+1
#     print("no.of vowels:",count)
# str=input("enter the string:")
# vowel_count(str)    
def vowel_count(str):
    count=0
    vowel=set("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowel:
            count=count+1
    print("no.of vowels:",count)
str=input("enter the string:")
vowel_count(str)    