a=int(input())
for i in range(10000):
    if a<2**i:
        b=i
        break
arr=[0]*b

def f(a):
    k=0
    a=bin(a)[2:]
    a=a.zfill(b)
    for j in range(len(a)):
        if a[j]=='1':
            global arr
            k+=arr[j]*(2**j)
            arr[j]+=1
    return k
def t(a):
    s=0
    for j in range(1,a+1):
        s+=j+f(j)
    return s
print(t(a))
