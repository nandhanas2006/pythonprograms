n=int(input("Enter the number of terms:"))
newlist=[]
even=[]
for i in range(n):
    b=int(input("Enter the numbers:"))
    newlist.append(b)
    if b%2==0:
        even.append(b)
print("The original list is:",newlist)
print("the even list is:",even)