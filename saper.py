from random import random

field_x = 20
field_y = 10
count_mine = 20
field = [[0 for i in range(field_x)] for j in range(field_y)]  # чистое поле
# for i in range(len(field)):
#     print(field[i])
i = 0
while i < count_mine:
    # print("i=%i x=%i y=%i" % (i,int(random() * field_x), int(random() * field_y)))
    x = int(random() * field_x)
    y = int(random() * field_y)
    if field[y][x] != -1:
        field[y][x] = -1
    else:
        continue
    i += 1
s_result = ""
for i in range(len(field)):
    for j in range(len(field[i])):
        s_result += "%3i" % field[i][j]
    s_result += '\n'
print(s_result)
print("\n")

# для эффективного единообразного заполнения поля предлагается расширить поле со всех сторон нулями
extended_field = [[0 for i in range(len(field[0]) + 2)] for j in range(len(field) + 2)]
# extended_field[1:len(field) + 1][1:len(field[0]) + 1] = field слайсы слайсов не работают
for i in range(1, len(field) + 1):
    extended_field[i][1:len(field[0]) + 1] = field[i - 1][0:len(field[0])]
    # for j in range(1, field_x + 1):
    #     extended_field[i][j] = field[i-1][j-1]
for i in range(1, len(extended_field) - 1):
    for j in range(1, len(extended_field[i]) - 1):
        if extended_field[i][j] != -1:
            count_bomb_by_cell = 0
            for m in range(i - 1, i + 2):
                for n in range(j - 1, j + 2):
                    if extended_field[m][n] == -1:
                        count_bomb_by_cell += 1
            extended_field[i][j] = count_bomb_by_cell
# field = extended_field[1:len(extended_field) - 1][1:len(extended_field[0]) - 1] работает не так как надо режет почему то сверху а не слева и справа
for i in range(len(field)):
    field[i] = extended_field[i + 1][1:len(extended_field[i + 1]) - 1]

s_result = ""
for i in range(len(extended_field)):
    for j in range(len(extended_field[i])):
        s_result += "%3i" % extended_field[i][j]
    s_result += '\n'
print(s_result)

s_result = ""
for i in range(len(field)):
    for j in range(len(field[i])):
        s_result += "%3i" % field[i][j]
    s_result += '\n'
print(s_result)
