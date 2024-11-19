arr = input()
count=0
m=0
for i in arr:
    if i=='s':
        count+=1
    else:
        m=max(m,count)
        count=0
print(max(m,count))
    
    
