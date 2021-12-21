list = [1,2, 4, 6, 7]
new = []
for i in list:
    new.append(i ** 2)
print(new)
n = 5
for i in range(n):
    for j in range(i):
        print('*', end='')
    print('')
for i in range(n,0, -1):
    for j in range(i):
        print('*', end='') 
    print('')

a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
c = int(input('Введите 3 число: '))
d = int(input('Введите 4 число: '))
max = a 
if b > max: max = b
if c > max: max = c
if d > max: max = d
print(max) 