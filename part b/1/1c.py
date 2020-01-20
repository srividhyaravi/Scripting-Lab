def maxi(l1,n):
    if n==0:
        return l1[0]
    return max(l1[n-1],maxi(l1,n-1))

n=int(input("enter range"))
l1=[]

for i in range(n):
    ele=int(input("enter val"))
    l1.append(ele)
print("max is " ,end="")
print(maxi(l1,n))