def atomicDictionary():
 atoms=     {
            "na":"sodium",
            "li":"lithium",
            "ag":"silver"
            }
 print("add a unique element ")
 key=input("enter the key")
 value=input("enter the value")
 atoms[key]=value
 print("add a duplicate value element")
 key1 = input("enter the key")
 atoms[key1]="sodium"
 print("add a duplicate key element")
 value1=input("enter the value")
 atoms["li"]=value1

 for i,j in atoms.items():
    print("key is ",i," value is ",j)

 print("the length of dictionary is ",len(atoms))
 f=0
 x=input("enter the value to search")
 for m,n in atoms.items():
     if n==x:
        print("the key of searched value is", m)
        f=1

 if f==0:
     print("not found")