'''l=0
r=0
arr=[1,3,4,2,2]
for i in arr:
    r+=i
for i in arr:
    l+=i
print(abs(l-r))

arr=input(eval)'''

l=[int(i) for i in input().split(" ")]
t=0
left=0
ans=-1
for i in range(0,len(l)):
    t-=l[i]
    if(t==left):
        ans=i
        break
    left+=l[i]
print(ans)