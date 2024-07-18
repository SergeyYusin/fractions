# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.

# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.

# Для проверки своего кода используйте модуль fractions.


frac1 = "1/2"
frac2 = "1/3"

# Введите ваше решение ниже

import fractions as fr

frac = fr.Fraction(frac1)
frac0 = fr.Fraction(frac2)
print('Сумма дробей:', frac + frac0)
print('Произведение дробей:', frac * frac0)
f = 0
r = 0
t = '1'
y = '1'
a = ''
b = ''
c = ''
d = ''
frac3 = ''
frac4 = ''
while frac1[f] != '/':
    a = a + frac1[f]
    f += 1

while frac2[r] != '/':
    c = c + frac2[r]
    r += 1

for i in range(len(frac1)):
    while frac1[i] != '/':
        b = b + frac1[i]
        t += '0'
        break
t = int(t) / int(10)
b = int(b) % int(t)

for _ in range(len(frac2)):
    while frac2[_] != '/':
        d = d + frac2[_]
        y += '0'
        break
y = int(y) / int(10)
d = int(d) % int(y)


def fractions(a, b, c, d):
    if b == d:
        frac4 = int(a) + int(c)
        print('Сумма дробей:', str(frac4) + '/' + str(d))
    elif b != d:
        frac4 = int(a) * int(d) + int(c) * int(b)
        d = int(b) * int(d)
        print('Сумма дробей:', str(frac4) + '/' + str(d))


fractions(a, b, c, d)
a = int(a) * int(c)
b = int(b) * int(d)
print('Произведение дробей:', str(a) + '/' + str(b))
