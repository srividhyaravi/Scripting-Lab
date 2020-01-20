diction = {
    "1ms17is074": "nidhi"
}
diction["1ms17is117"] = "srivi"
diction["1ms17is006"] = 'sid'

print(diction)

print("dictionary values after sorting")
asc=list(diction.values())
asc.sort()
print(asc)


delval = []
for i,j in diction.items():
    if j[0] == 's':
        delval.append(i)

print(" dictionary after deleting the name starting with 's'")
for i in delval:
    del diction[i]

print(diction)




