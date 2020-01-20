l1=[]

print("enter the no of elements")
n=int(input())

for i in range(n):
    l1.append(int(input()))

print(l1)

print(min(l1))
print(max(l1))

print("enter the element u wnat to enter")
ele=int(input())
l1.append(ele)
print(l1)

print("enter the elemrnt to delete")
ele=int(input())
try:
    l1.remove(ele)
except ValueError:
    print("no such elemrnt present")

print(l1)

print("enter the element yow wnt to search")
ele=int(input())
if ele in l1:
    print("present")
else:
    print("absent")



