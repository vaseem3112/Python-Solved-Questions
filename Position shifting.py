l=[int(i) for i in input().split(" ")]
d=3
ans=l[-d:]+l[:-d]
print(ans)