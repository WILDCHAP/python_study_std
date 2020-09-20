
tuple1 = ('a', 'b', 'c', 1, 'd', '5', 'e', 3, 'a')

print(tuple1[2], len(tuple1), tuple1.count('a'), tuple1.index(1))

for t in tuple1:
    print(t, end=' ')

a = set(tuple1)
print(type(a), a)
a = tuple(a)
print(type(a), a)
