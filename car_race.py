from math import floor
sequence_of_numbers = input().split()
my_list = []
time_of_first_car = 0.00
time_of_second_car = 0.00
idx_of_middle = floor(len(sequence_of_numbers) / 2)

for idx in sequence_of_numbers:
    integer_num = int(idx)
    my_list.append(integer_num)

for num in my_list:
    time_of_first_car += num
    if num == 0:
        time_of_first_car *= 0.80
    if num[5]:
        reverse_list = my_list[::-1]
        continue

my_list.pop(idx_of_middle)
print(my_list)