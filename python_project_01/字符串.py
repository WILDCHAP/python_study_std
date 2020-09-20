s = "hellow string"

print(len(s), s.index('s'), s.find('1'), s.count('l'))

a = ['1', '2', '3']

b = s.join(a)

print(b)

c = b.split("he", 1)    # 分割成两个

print(c)

print(s.replace("string", "python"))