a = {'1':1, 2:'aaa', '3':'b'}
a[3] = 'ha'
a['3'] = 2
a.pop('1')
print(len(a))

for key, val in a.items():
    print(key, val)
for key in a.keys():
    print(key)
for val in a.values():
    print(val)

print(a[2])