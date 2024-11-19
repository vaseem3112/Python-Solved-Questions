s=input()
st=""
for i in s:
    if(i=='a'):
        st=st+'b'
    elif(i=='b'):
        st=st+'a'
    else:
        st=st+i
print(st)