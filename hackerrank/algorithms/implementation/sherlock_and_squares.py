import math


def sherlock_and_squares(num1, num2):
    return len([i for i in range(num1, num2+1) if math.sqrt(i) == int(math.sqrt(i))])

# print(sherlock_and_squares(64,822)) # 21
# print(sherlock_and_squares(16,368)) # 16
# print(sherlock_and_squares(36,423)) # 15
# print(sherlock_and_squares(144,658)) # 14
# print(sherlock_and_squares(121,743)) # 17
#



with open('sherlock_and_squares_input05.txt') as f:
    inputs_file = f.readlines()

with open('sherlock_and_squares_output05.txt') as f:
    outputs_file = f.readlines()

number_of_ops = inputs_file[0]
del inputs_file[0]

for i in range(int(number_of_ops.strip())):
    num1, num2 = inputs_file[i].strip().split(' ')
    num1, num2 = int(num1), int(num2)
    print(i)
    if sherlock_and_squares(num1, num2) != int(outputs_file[i].strip()):
        print(f'{num1}, {num2}, mine:{sherlock_and_squares(num1, num2)}, {outputs_file[i]}')
