sequence_of_numbers = input().split()

my_list = []
left_car = 0.00
right_car = 0.00

idx_of_middle = len(sequence_of_numbers) // 2

for idx in sequence_of_numbers:
    integer_num = int(idx)
    my_list.append(integer_num)

for idx, number in enumerate(my_list):
    if idx < idx_of_middle:
        left_car += number
        if number == 0:
            left_car *= 0.80

my_list = my_list[::-1]

for idx, number in enumerate(my_list):
    if idx < idx_of_middle:
        right_car += number
        if number == 0:
            right_car *= 0.80

if left_car < right_car:
    print(f"The winner is left with total time: {left_car:.1f}")
elif right_car < left_car:
    print(f"The winner is right with total time: {right_car:.1f}")
