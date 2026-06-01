a={1,2,3,4}
b={5,6,7}
a.add(5)
a.update([6,7])
a.remove(4)
#discard is a inbuilt function works like same as remove but if the element doesn't exist then it doesn't show error
a.discard(5)
a.pop()#delete last element
a.clear()#delete all elements
print(a.union(b))#it combines the two sets
print(a.intersection(b))#returns common elements
print(a.difference(b))#difference between two sets

print(a)