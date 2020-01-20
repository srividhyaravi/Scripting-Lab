def remove(li):
    final_list=[]
    for num in li:
            if num not in final_list:
                final_list.append(num)
    return final_list
li=[2,3,4,5,2,3,4,5,6,7,8]
b=remove(li)
print(b)
a=[x for x in b if x%2==0]
print(a)
a.reverse()
print(a)
