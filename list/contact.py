c={}
print("1.add a contact")
print("2.delete a contact")
print("3.edit a contact")
print("4.search a contact") 
print("5.list all contacts")
print("6.exit")    
c=int(input("enter the choice"))
while c!=6:
    if c==1:
        name=input("name")
        phn=int(input("phn"))
        c[name]=phn            