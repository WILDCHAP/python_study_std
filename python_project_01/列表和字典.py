a = [{'a':1,'b':2},
     {'a':3,'d':4}]

for i in a:
    print(i)
    for key,val in i.items():
        print(key, val)