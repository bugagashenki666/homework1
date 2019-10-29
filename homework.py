# task1 is power of 2
import math

print("# task1 is power of 2")
print("Введите целое число")
n = int(input())
i = n
power = 0
while i % 2 == 0:
    i = i / 2
    power += 1
if i == 1:
    print("Число " + str(n) + " является целой степенью " + str(power) + " числа 2")
else:
    print("Число " + str(n) + " не является целой степенью числа 2, но является нецелой степенью " + str(
        math.log(n, 2)) + " числа 2")

# task2 print all integer numbers between a and b ending 4
print("# task2 print all integer numbers between a and b ending 4")
print("Введите верхнюю границу диапазона:")
a = int(input())
print("Введите нижнюю границу диапазона:")
b = int(input())
end_digit = '4'
for k in range(a, b + 1):
    s = str(k)
    if s[len(s) - 1] == end_digit:
        print(k)

# task3 calculate factorial of n
print("# task3 calculate factorial of n")
print("Введите число, от которого нужно посчитать факториал")
n = int(input())
f = 1
i = 1
while i <= n:
    f = f * i
    i += 1
print("factorial(" + str(n) + ")=" + str(f))

# task4 calculate the k-th of Fibonacci number
print("# task4 calculate the k-th of Fibonacci number")
print("Введите номер необходимого числа фибоначчи:")
k = int(input())
k_fibonacci = 1
prev = 1
prev_prev = 0
i = 2
while i < k:
    prev_prev = k_fibonacci
    k_fibonacci = k_fibonacci + prev
    prev = prev_prev
    i += 1
print(str(k) + "-е число Фибоначчи = " + str(k_fibonacci))

# task5 to examinate string consists of symbols 'a', 'b', 'c' only
print("# task5 to examinate string consists of symbols 'a', 'b', 'c' only")
print("Введите проверяемую строку")
s = input()
for c in s:
    if c != 'a' and c != 'b' and c != 'c':
        print("строка " + s + " содержит символы отличные от 'a', 'b', 'c'")
        break
else:
    print("строка " + s + " состоит только из символов 'a', 'b', 'c'")

# task6 calculate k times some expression
print("#task6 calculate k times some expression")
print("Введите количество выражений:")
k = int(input())
i = 0
while i < k:
    print("Введите число")
    a = float(input())
    print("Введите число")
    b = float(input())
    print("Введите операцию")
    op = input()
    i += 1
    if op == "+":
        print(str(a) + "+" + str(b) + "=" + str(a + b))
    elif op == "-":
        print(str(a) + "-" + str(b) + "=" + str(a - b))
    elif op == "*":
        print(str(a) + "*" + str(b) + "=" + str(a * b))
    elif op == "/":
        print(str(a) + "/" + str(b) + "=" + str(a / b))
    elif op == "%":
        print(str(a) + "%" + str(b) + "=" + str(a % b))
    elif op == "//":
        print(str(a) + "+" + str(b) + "=" + str(a // b))
    elif op == "**":
        print(str(a) + "**" + str(b) + "=" + str(a ** b))
    else:
        print("Неизвестная операция")
