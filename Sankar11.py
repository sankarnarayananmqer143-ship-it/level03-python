print("takshashila university")
print("ungur,tindivanam")
print("----------------------")
print("STUDENT MARK LIST")
print("----------------------")
no=int(input("enter the register no:"))
name=str(input("enter the student name:"))
m1=int(input("enter the python mark:"))
m2=int(input("enter the DBMS mark:"))
m3=int(input("entert the Test automation mark:"))
total=m1+m2+m3
print("Total mark:",total)
avg=total/3
print("Average mark:",avg)
if(m1>=40,m2>=40,m3>=40):
    print("Result:pass")
else:
    print("Result:fail")
if(total>=250):
    print("Grade:O Grade")
elif(total>=200):
    print("Grade:A Grade")
else:
    print("Grade:B Grade")
