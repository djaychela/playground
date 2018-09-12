def sortStudents(students):
    students.sort(key=lambda s: s.split()[-1])
    return students


print(sortStudents(["John Smith",
                    "Jacky Mon Simonoff",
                    "Lucy Smith",
                    "Angela Zimonova"]))
