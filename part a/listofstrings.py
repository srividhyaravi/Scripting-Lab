list1=['the','2','cat','8','nest','had','great']
list2=[x for (i,x) in enumerate(list1) if i%2!=0]
print(list2)
for i in range(0,len(list1)):
    if((i+1)%3 == 0):
        print(list1[i].upper())
        #print(list1)

for i in range(0,len(list1)):
    print(list1[i][::-1])