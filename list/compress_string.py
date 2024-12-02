s="aaabbcccd"

num=1
while num<=limit:
    temp=num
    ex=len(str(temp))
    sum_digit=0
    temp=num
count_list=[]
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if s[i]==s[j]:
            c+=1
    count_list.append(c) 
f=none
for i in range(len(s)):
    if count_list[i]==1:
        f=s[i] 
        break
print("first non repeated value",f)          
