from math import ceil
sequence_of_numbers = input().split()

time_of_first_car = 0.00
time_of_second_car = 0.00
idx_of_middle = ceil(len(sequence_of_numbers) / 2)
sequence_of_numbers.pop(idx_of_middle)

for idx in sequence_of_numbers:
    integer_num = int(idx)

print(sequence_of_numbers)