set1={'ram','shyam','nikhil'}
set2={'nikhil','jiya','akash'}
set3={'ankur','pradeep'}
print(set1.union(set2))
print(set1.union(set2,set3))
print(set1 | set2)
set1.update(set2)
print(set1)
print(set1.intersection(set2,set3)) 
print(set1.intersection(['monday','tuesday']))
print(set1 & set2 & set3)
print(set1)
set2.clear()
print(set2)
del set2
print("mike")
print(set1-set2)
print(set1.difference(('mohan','ram')))
print(set1.difference(set2,set3))
print(set1.symmetric_difference(set2))
print(set1 ^ set2^ set3)
