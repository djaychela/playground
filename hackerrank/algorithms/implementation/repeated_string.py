# intuitive solution, takes way too long for test case of 1000000000000
def repeated_string(string, length):
    new_string = list((string * (length // len(string) + 1))[:length])
    return new_string.count('a')


def repeated_string_2(string,length):
    a_list = list(string)
    a_count = a_list.count('a')
    repeats = length // len(string)
    remains = length % len(string)
    number_of_as = a_count * repeats + (a_list[:remains].count('a'))
    return number_of_as


print(repeated_string_2('aba', 10))
print(repeated_string_2('a', 1000000000000))
