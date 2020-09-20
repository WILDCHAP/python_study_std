import 九九乘法表 as jj

jj.f1()
print(jj.name)

a = ['a', 'b', 'c', 'd', 'a', 'c']
#a.sort()
a.sort(reverse=True)
a.reverse()
a.insert(0,'k')
b = set(['a', 'b', 'c', 'd', 'a', 'c'])
print(a, b)
print(a.index('a'))
a.remove('k')
print(a)
del a[3]
print(a)
k1 = a.pop()
print(k1)
a.append('z')
print(a)