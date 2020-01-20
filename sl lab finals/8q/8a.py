atoms={"H":"hydrogen",
       "Li":"lithium",
       "He":"helium",
        "B":"boron"
       }

print("enter existing element")
symbol=input()
print("enter element name")
element=input()

atoms[symbol]=element

print(atoms)

print("enter new element")
symbol=input()
print("enter element name")
element=input()

atoms[symbol]=element

print(atoms)

print("length of dictionary is",len(atoms))

print("enter the element you want to search")
element=input()

if element in atoms:
    print("element found and it is",atoms[element])
else:
    print("not found")