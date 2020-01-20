class SentenceReverser:
    vowels=["a","e","i","o","u"]
    sentence=""
    reverse=""
    vowelcount=0
    def __init__(self,sentence):
        self.sentence=sentence
        self.reverseSentence()
    def reverseSentence(self):
        self.reverse="".join(reversed(self.sentence.split()))
    def getvowelcount(self):
        self.vowelcount=sum(s in self.vowels for s in self.sentence.lower())
        return self.vowelcount
    def getreverse(self):
        return self.reverse

items=[]
for i in range(3):
    reverser=SentenceReverser(input("enter sentence"))
    items.append(reverser)
    print(reverser.reverse)
print("sorted descending vowel count")
for i in sorted(items,key=lambda items:items.getvowelcount(),reverse=True):
    print(i.getreverse(),"->",i.getvowelcount())