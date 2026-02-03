def racing_calc(steps):
    total = 0.0
    for num in steps:
        total += num
        if num == 0:
            total *= 0.80
    return total


numbers = [int(x) for x in input().split()]
mid = len(numbers) // 2

left_car = numbers[:mid]
right_car = numbers[mid+1:][::-1]

left_car_time = racing_calc(left_car)
right_car_time = racing_calc(right_car)

if left_car_time < right_car_time:
    winner = "left"
    print(f"The winner is {winner} with total time: {left_car_time:.1f}")
else:
    winner = "right"
    print(f"The winner is {winner} with total time: {right_car_time:.1f}")
    