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

extended_field = [[field[i][j] for i in range(0, field_x + 2) if 1 < i < field_x + 1] for j in range(0, field_y + 2) if
                  1 < j < field_y + 1]

for i in range(len(extended_field)):
    for j in range(len(extended_field[i])):
        s_result += "%3i" % extended_field[i][j]
    s_result += '\n'
print(s_result)
