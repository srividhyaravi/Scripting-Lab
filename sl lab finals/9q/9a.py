class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        print("name is ",self.name)
        print("age is ",self.age)
        print("marks are ",self.marks)

    def accept(self):
        print("enter name")
        name=input()
        self.name=name

        print("enter age")
        age = (input())
        self.age = age

        for i in range(3):
            self.marks.append(int(input("enter marks"+str(i)+" :")))

obj=student('nidhi','20',[99,100,99])
obj.display()

obj1=student('','' ,[])
obj1.accept()
obj1.display()
