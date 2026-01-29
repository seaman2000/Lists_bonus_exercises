sequence_of_numbers = input().split()
text = input()

text_list = list(text)
message = ""

for number in sequence_of_numbers:
    digit_sum = 0
    for digit in number:
        digit_sum += int(digit)

    index = digit_sum % len(text_list)
    message += text_list[index]
    text_list.pop(index)

print(message)