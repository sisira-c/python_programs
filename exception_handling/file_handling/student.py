filename="student_details.txt"
f=open(filename,"w")
n=int(input("enter the number:"))
for i in range(1,n+1):
    print(f"enter the details of student{i}")
    name=input("name :")
    age=int(input("age :"))
    grade=input("grade :")
    f.write(f"student{i+1}:\n")
    f.write(f"name: {name}\n")
    f.write(f"age: {age}\n")
    f.write(f"grade: {grade}\n")
    f.write("-"* 20 + "\n")
print(f"student details have been written to {filename}")    