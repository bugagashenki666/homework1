# create list of string with equal start and end character
'''
in_s = "Bla-bla-blab\n" \
       "Aaa aa ak\n" \
       "Ddd ff ddd\n" \
       "dddff\n" \
       "hhh ggg h"
input_list = in_s.split("\n")
print("Входные данные:" + str(input_list))
output_list = [s for s in input_list if s[0].lower() == s[- 1].lower()]
# output_list = []
# for s in input_list:
#     if s[0].lower() == s[-1].lower():
#         output_list.append(s)
print("Результат" + str(output_list))

# generate list of numbers that are the power of number 2 and have length k
k = 10
numbers_power_2 = [2 ** k for k in range(k)]
print("Result: " + str(numbers_power_2))

# it has list of integer's lists. print row only with positive values
in_l = [[1, 2, 3], [-1, 2, 3], [333, 3, 2], [-1, -2, -3], [0, 1, 0]]
for row in in_l:
    for n in row:
        if n < 0:
            break
    else:  # относится к break если что
        print(str(row))

# print("\n".join(str([col for col in row if col > 0]) for row in in_l))# не работает
# print("\n".join(str(col) for row in in_l for col in row if col >= 0))#не  работает

# it has dimension of 2. print column that has the sum's maximum of values
input_list = [[1, -2, -5, 3, -44, 25, 3000, 4000],
              [23, -23, 4, 4, 5, -45, -1000, -2000],
              [-81, -33, 2, 3, 4, -99, 3000],
              [100, 1000, 200, 300, 2000, 500, 100000, 1000000, 1000000, 1000000000]]
sum_cols = [0 for x in range(max([len(row) for row in input_list]))]
# создаем список и инициализируем его нулями(количество элементов в строках исходного массива разное ).
for row in input_list:
    for idx_col in range(len(row)):
        sum_cols[idx_col] = sum_cols[idx_col] + row[idx_col]
print("Суммы столбцов: " + str(sum_cols))
print("Максимальную сумму имеет столбец с индексом %i и эта сумма=%i" % (sum_cols.index(max(sum_cols)), max(sum_cols)))
# idx_max = 0
# for i in range(len(sum_cols)):
#     if sum_cols[i] > sum_cols[idx_max]:
#         idx_max = i
# print("Максимальную сумму имеет столбец с индексом " + str(idx_max) + " и эта сумма = " + str(sum_cols[idx_max]))

# check matrix ix symmetrical of diagonals
k = 5
matrix_symmetrical = [[i + j for i in range(k)] for j in range(k)]  # [[i*j for i in range(k)] for j in range(k)]
matrix_not_symmetrical = [[i ** j for i in range(k)] for j in range(k)]
cur_matrix = matrix_not_symmetrical
is_diagonal_symmetrical = True
for idx_row in range(len(cur_matrix)):
    for idx_col in range(len(cur_matrix[idx_row])):
        if cur_matrix[idx_row][idx_col] != cur_matrix[idx_col][idx_row]:
            is_diagonal_symmetrical = False
            break
    if not is_diagonal_symmetrical:
        break
if not is_diagonal_symmetrical:
    print("матрица %s несимметрична относительно левой диагонали" % str(cur_matrix))
else:
    print("матрица %s симметрична относительно левой диагонали" % str(cur_matrix))

matrix_absolute_symmetrical = [[1 for i in range(k)] for j in range(k)]
cur_matrix = matrix_absolute_symmetrical
k = len(cur_matrix)
is_diagonal_symmetrical = True
for idx_row in range(len(cur_matrix)):
    for idx_col in range(len(cur_matrix[idx_row])):
        if cur_matrix[idx_row][idx_col] != cur_matrix[k - 1 - idx_row][k - 1 - idx_col]:
            is_diagonal_symmetrical = False
            break
    if not is_diagonal_symmetrical:
        break

if not is_diagonal_symmetrical:
    print("матрица %s несимметрична относительно правой диагонали" % str(cur_matrix))
else:
    print("матрица %s симметрична относительно правой диагонали" % str(cur_matrix))

# print snake from array
# 1 2 3
# 8 9 4
# 7 6 5
'''
# group sequence for even: 2*2, 3*4, 5*4, 7*4...= 2*2*k,(2k+1)*4,k = 1,2,3,4,5,....
# group sequence for not even: 1*1,2*4,4*4,6*4...= 1*1*k, 2k*4, k = 1,2,3,4,5,...

k = 12
l = [[0 for i in range(k)] for j in range(k)]
if k < 3:
    print("k  должно быть больше или равно 3")
    exit(1)
# разбивка по участкам длиной k-1
sequence = ()
if k % 2 == 0:
    sequence = list(range(k - 1, 2, -2))
    sequence.append(2)
else:
    sequence = list(range(k - 1, 1, -2))
    sequence.append(1)
# print(sequence)
current_length = sequence[0]
max_steps = k * k
count_of_full_rotation = 0# количество полных оборотов по часовой стрелке
current_number = 1# используется при одном полном обороте по часовой стрелке
idx_row = 0
idx_col = 0
current_number2 = 1# используется при всех оборотах по часовой стрелке
while current_number2 < max_steps:
    l[idx_row][idx_col] = current_number2
    if current_number <= current_length:
        idx_col += 1
    elif current_length < current_number <= 2 * current_length:
        idx_row += 1
    elif 2 * current_length < current_number <= 3 * current_length:
        idx_col -= 1
    elif 3 * current_length < current_number < 4 * current_length:
        idx_row -= 1
    elif current_number == 4 * current_length:
        idx_col += 1
        current_number = 0
        count_of_full_rotation += 1
        current_length = sequence[count_of_full_rotation]
        if count_of_full_rotation == len(sequence) - 1:# печать центра
            if current_length == 1:# для нечетных k
            # if k%2 == 1:
                l[idx_row][idx_col] = current_number2 + 1
            elif current_length == 2:# для четных k
            # if k%2 == 0
                l[idx_col][idx_row] = current_number2 + 1
                l[idx_col][idx_row + 1] = current_number2 + 2
                l[idx_col + 1][idx_row + 1] = current_number2 + 3
                l[idx_col + 1][idx_row] = current_number2 + 4
            break
    current_number += 1
    current_number2 += 1
s_result = ""
for i in range(len(l)):
    for j in range(len(l[i])):
        s_result += "%5i " % l[i][j]
    s_result += '\n'
print(s_result)
