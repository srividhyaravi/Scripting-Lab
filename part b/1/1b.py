from collections import Counter
def word_Count(fname):
    with open(fname) as f:
        return Counter(f.read().split())
print("freq of words is ",word_Count("aaa.txt"))