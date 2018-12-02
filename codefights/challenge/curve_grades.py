import statistics

def curveGrades(percentages):
    dev = statistics.stdev(percentages)
    centre = statistics.mean(percentages)
    output_list = []
    for stat in percentages:
        devs = round((stat-centre) // dev) +3
        letter = 'FDCBA'[devs]
        output_list.append(letter)
    return output_list



percentages = [79, 92, 93, 83, 82]
output = ["D",
         "B",
         "A",
         "C",
         "C"]

print(curveGrades(percentages) == output)

percentages = [24, 30, 44, 28, 34]
output = ["D",
         "C",
         "A",
         "C",
         "B"]

percentages = [82, 5, 20, 63, 91, 60, 93, 52, 17, 16]
output = ["B",
         "D",
         "C",
         "B",
         "A",
         "B",
         "A",
         "B",
         "C",
         "D"]

percentages = [4, 88, 45, 87, 14, 18]
output = ["D",
         "A",
         "B",
         "A",
         "C",
         "C"]

percentages = [10, 20, 30, 50, 60, 60, 75, 77, 80, 81, 85, 90, 91, 95, 97, 100]
output = ["F",
         "D",
         "D",
         "C",
         "C",
         "C",
         "B",
         "B",
         "B",
         "B",
         "B",
         "B",
         "B",
         "B",
         "A",
         "A"]

percentages: [76, 5, 63, 52, 72]
output = ["B",
 "D",
 "B",
 "C",
 "B"]


