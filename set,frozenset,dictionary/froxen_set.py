set1=frozenset({10,20,30,40,50})
set2=frozenset({1,2,3,4,5,50,40})
print("original set1=",set1)
print("original set2=",set2)

a=set1.union(set2)
print(a)

b=set2.intersection(set1)
print(b)

c=set2.issubset(set1)
print(c)

d=set2.issuperset(set1)
print(d)