s="pythonpy"
count_list=[]
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if s[i]==s[j]:
            c+=1
    count_list.append(c)
    f=None
for i in range(len(s)):
    if count_list[i]==1:
        f=s[i]
        break
print("first non repeat value",f)    
                