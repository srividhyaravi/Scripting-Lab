from functools import reduce
l1=[]
print("enter no of elements")
n=int(input())
i=0
while i<n:
    ele=int(input("enter number"))
    l1.append(ele)
    i=i+1

print(l1)
newl1=[i*i for i in l1]
print(newl1)

sum1=reduce((lambda x, y:x+y),l1)
sum2=reduce((lambda x, y:x+y),newl1)

print(sum1)
print(sum2)