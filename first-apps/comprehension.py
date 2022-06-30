names = ['Duda', 'Rafa', 'Cris', 'Yuri']
names2 = [name for name in names if 'r' in name]
print(names2)

# Saída
# ['Cris', 'Yuri']

square = [x*x for x in range(11)]
print(square)

odds = [x for x in range(1,50) if x % 2 != 0]
print(odds)
