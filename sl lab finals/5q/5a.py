def ctof(c):
    f=(9/5)*c+32
    history.append((str(c)+' deg c ',str(f)+' deg f '))
    return f

def ftoc(f):
    c=(f-32)*(5/9)
    history.append((str(f) + ' deg f ' , str(c) + ' deg c '))
    return c

def ctok(c):
    k=c+273.15
    history.append((str(c)+' deg C', str(k)+' deg K'))
    return k
history=[]

while(True):
 ch=int(input("enter 1 to c to f enter 2 to f to c"))
 print()
 if(ch==1):
    c=float(input("enter celsius value"))
    print("fahrenhiet is ",ctof(c))
 elif ch==2:
    c = float(input("enter fahrenhiet value"))
    print("fahrenhiet is ", ftoc(c))
 elif ch==3:
    c = float(input("enter celsius value"))
    print("fahrenhiet is ", ctok(c))
 elif ch == 4:
    print("History of conversions:\n", history)
 elif ch == -1:
     break

 else:
    print("invaid choice")