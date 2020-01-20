class reversee:
    def __init__(self,s):
        self.s=s

    def rev(self):
        sen=self.s
        w=sen.split(" ")
        w.reverse()
        for i in w:
            print(i,end=" ")
        print()

c=0
s=[]

while c<3:
    sen=input("enter a sentence")
    c=c+1
    s.append(sen)

s1=sorted(s,key=lambda x:sum(ch in 'AEIOUaeiou' for ch in x),reverse=True)

for i in s1:
    ob=reversee(i)
    ob.rev()