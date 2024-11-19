def occured(arr):
    a= {}
    for i in arr:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    return a

arr = eval(input())
output = occured(arr)

for j, k in output.items():
    print(f"{j}>>{k}")