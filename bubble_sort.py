# bubble sort


data = [7, 5, 1, 2, 3, 4, 6]

incomplete = True
while incomplete:
    index = 0
    incomplete = False
    while index < len(data) -1:
        if data[index] > data[index + 1]:
            data[index], data[index + 1] = data[index + 1], data[index]
            print(data)
            incomplete = True
        index += 1

