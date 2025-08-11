print("Sankar computer mart")
print("Nehru street,villupuram")
print("-----------------------")
print("     BILL RECEIPT      ")
print("-----------------------")
no=str(input("Enter the item no:"))
na=str(input("Enter the particular:"))
rate=int(input("Enter the rate:"))
quty=int(input("Enter the Quantity:"))
total=rate*quty
print("Total amount in rupees:",total)
if(total>=100000):
    GST=total*10/100
    print("GST:",GST)
elif(total>=50000):
    GST=total*5/100
    print("GST:",GST)
elif(total>=20000):
    GST=total*3/100
    print("GST:",GST)
else:
    GST=total*2/100
    print("GST:",GST)
