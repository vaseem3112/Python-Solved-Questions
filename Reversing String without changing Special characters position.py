#Write a function to return a string which contains alphabets and special characters your task is swap the positions of only alphabets keeping the special characters position unchanged.
#Input:PYTH%&ON

str=input()
st=" "
result=" "
for i in str:
    if i.isalpha():
        st=st+i

strl=st[::-1]
a=0
for i in range(len(str)):
    if str[i].isalpha():
        result=result+strl[a]
        a=a+1
    else:
        result=result+str[i]
print(result)