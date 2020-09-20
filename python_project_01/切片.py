a = ['a', 'b', 'c', 'd', 'e', 'f']

print(a[::2])  # 以2为步长

b = a[:]

b[1] = 'k'
print(a)

#利用切片达到逆序效果
print(a[-1::-1])
