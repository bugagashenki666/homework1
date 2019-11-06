# print snake from array
# 1 2 3
# 8 9 4
# 7 6 5

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
