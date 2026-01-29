numbers = input().split(", ")
my_list = []
zero_counter = 0

for each_number in numbers:
    integer_num = int(each_number)
    if integer_num != 0:
        my_list.append(integer_num)
    else:
        zero_counter += 1
for _ in range(zero_counter):
    my_list.append(0)

print(my_list)