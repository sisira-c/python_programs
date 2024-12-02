number={0:"zero",1:"one",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
positional_num={0:"ones",1:"tens",2:"hundred",3:"thousand",4:"tenthousand",5:"lakh"}
n=input("enter the number")
r=""
l=len(n)-1
for i in n:
    key=int(i)
    value=number[key]
    r=r+" "+ value+ " "+positional_num[l]
    l-=1
print("the number is",n)
print("number place value is",r)