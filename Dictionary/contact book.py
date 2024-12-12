contact={}
while True:
    choice=int(input("\n 1.add a contact \n 2.delete a contact \n 3.edit a contact \n 4.search a contact \n 5.list all contacts \n 6.exit \n enter your choice:"))
    if choice==1:
        name=input("name :")
        phone=input("phone number:")
        contact[name]=phone
    elif choice==2:
        del_contact=input("enter the contact to be deleted:")
        if del_contact in contact:
            contact.pop(del_contact)
            print('name \t\t contact number')
            for key in contact:
                print(f"{key}\t\t{contact.get(key)}")

        else:
            print("no contact found!")
    elif choice==3:
        edit_contact=input("enter the contact to be edited:")
        if edit_contact in contact:
            phone=input("enter the phone number:")
            contact[edit_contact]=phone
            print("contact updated")
            print("name \t\t{contact number")
            for key in contact:
                print(f'{key}\t\t{contact.get(key)}')
        else:
            print("no contact found!")
    elif choice==4:
        search_contact=input("enter the contact to be searched:") 
        if search_contact in contact:       
            print("search_contact,"'s contact number is',contact[search_contact])
        else:
            print("no contact found!")
    elif choice==5:
        if not contact:
            print("contact book is empty!")
        else:
            print("name \t\t contact number")
            for key in contact:
                print(f"{key}\t\t{contact.get(key)}")
    else:
        break                            


