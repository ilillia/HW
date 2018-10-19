print('--------')
print('Задача 1')
print('--------')

print('Введите последовательно все три стороны треголька')

a = float(input())
b = float(input())
c = float(input())
d = float(2.00)
e = float(0.5)


p = float((a + b + c) / d)
S = float((p*(p-a)*(p-b)*(p-c)) ** e)
s = round(S , 1)
print('Площадь треугольника ранвна', s)

print('--------')
print('Задача 2')
print('--------')

a = 'bad'
b = 'boy'

print(a)
print(b)

print('--------')

a , b = b , a 

print(a)
print(b)

print('--------')

print('--------')
print('Задача 3')
print('--------')

a = 5
b = 6
print(a)
print(b)
print('--------')

b = b * a / b
a = (a + a + a + a + a + a) / b

round(a)
round(b)

print(a)
print(b)

(*) найти количетсво минут в неделе 

N = 7
D = 24
T = 60
M = 60
S = M*T*D*N
print('в неделе столько секунд', S)

print('''
--------
Задача 4
--------
''')

x = float(input('>>>'))
x = round(x ** 2) if x // 2 == x / 2 else round(x * 2)
print(x)