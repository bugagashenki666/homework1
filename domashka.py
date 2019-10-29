# Является ли число степенью двойки

a = int(input())
while a % 2 == 0:
    a //= 2
print(a == 1)

# Написать все числа в промежутке от а до б,которые оканчиваются на 4


a, b = int(input()), int(input())
if b % 10 > 4:  # если конец отрезка имеет в разряде единиц число большее, чем 4 -
    b -= b % 10 - 4  # - приводим его к самому ближайшему числу оканчивающемся на 4 слева

elif b % 10 < 4:  # анологично, если в разряде единиц число меньше, чем 4
    b = b - b % 10 - 6

while b >= a:  # пока конец левого отрезка больше правого, вычитаем 10 -
    print(b)  # - Эти числа и будут искомыми. Сразу принтуем.
    b -= 10
else:  # сюда пойдем только если в отрезке таких чисел нет
    print(None)

# факториал с циклом


i = int(input())
answer = 1
for b in range(1, i + 1):
    answer *= b
print(answer)

# фибаначи c циклом
one = two = 1
a = int(input())
count = 0
while count < a - 2:  # первые два члена записаны, поэтому нам не нужно делать a операций
    count += 1
    one, two = two, one + two
print(two)

# проверить что строка состоит только из букв a,b,c


a = input()
Flag = True
for i in a:
    if not (i in 'abc'):
        Flag = False
print(Flag)

# Калькулятор
col =int(input())
for i in range(col):
    a = int(input())
    b = int(input())
    c = input()
    if c == '-':
        print(a - b)
    elif c == '//':
        print(a // b)
    elif c == '*':
        print(a * b)
    # и так далее
