def correctScholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents).issubset(scholarships) and set(scholarships).issubset(allStudents) and len(scholarships) < len(allStudents)




print(correctScholarships(bestStudents = [3, 5], scholarships = [3, 5, 7], allStudents = [1, 2, 3, 4, 5, 6, 7]))