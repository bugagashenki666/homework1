# task1 print string with deleted repeating
print("#task1 print string with deleted repeating")
s = "aaaabbbbcccddeeeeeeffff"
s = s + "\n"
new_s = ""
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        new_s = new_s + s[i]
print(new_s)

# task2 calculate the numbers of entry upper and lower characters
print("#task2 calculate the numbers of entry upper and lower characters")
s = "AAAAAvvvvvvBBBBBssssssTTTTTTSSSSS"
count_lower = 0
count_upper = 0
for c in s:
    if c.isupper():
        count_upper += 1
    elif c.islower():
        count_lower += 1
print("Count lower =" + str(count_lower) + " count upper =" + str(count_upper))

# task3 print all numbers
print("#task3 print all numbers from string")
s = "166666bla-bla-bla 1480000000 bla-blabla ....40000 bla-bla-bla500...00dfgdfgdfgd464564.56....45mmmm0.7778..........."
s = s + "\n"
count_digit = 0
start_digit = 0
flag_reverse_deleting_point = True
for i in range(len(s)):
    if s[i].isdigit() or (s[i] == '.' and count_digit > 0):
        if count_digit == 0:
            start_digit = i
        count_digit += 1
    elif count_digit != 0:
        result_s = s[start_digit:start_digit + count_digit]
        while result_s[-1] == '.':
            result_s = result_s[0:-1]
        if flag_reverse_deleting_point:
            result_s = result_s[-1:-len(result_s) - 1:-1]
        result_s = result_s.replace(".",'', result_s.count('.') - 1)
        if flag_reverse_deleting_point:
            result_s = result_s[-1:-len(result_s) - 1:-1]
        print(float(result_s))
        count_digit = 0
