n=[1,2,3,4,5,2,4,"hi",'python']
uelements=[]
for i in n:
  if i not in uelements:
     uelements.append(i)
print(uelements)