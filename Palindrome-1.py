#Method 1:
def palin(a):
    a = ''.join(b for b in a if b.isalnum())
    a = a.lower()
    rev = a[::-1]
    if a == rev:
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")
a = input("Enter a string: ")
palin(a)

#Method 2:
a = input("Enter a string: ")
i=0
f=0
j=len(a)-1
while (i<j):
    if (a[i]==a[j]):
        i+=1
        j-=1
    else:
        f=1
        break
if(f==0):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

