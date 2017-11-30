def angry_professor(num_of_students, student_list):
    on_time = 0
    for student in student_list:
        if student <= 0:
            on_time += 1
    if on_time >= num_of_students:
        return 'NO'
    return 'YES'


def angry_professor_2(num_of_students, student_list):
    on_time = sum([1 if student <= 0 else 0 for student in student_list])
    return 'YES' if on_time < num_of_students else 'NO'


print(angry_professor_2(3, [-1, -3, 4, 2]))
print(angry_professor_2(2, [0, -1, 2, 1]))

print(angry_professor(3, [-1, -3, 4, 2]))
print(angry_professor(2, [0, -1, 2, 1]))
#
# for _ in range(input()):
#     n, k = map(int, raw_input().split())
#     a1 = filter(lambda x:x <= 0, map(int, raw_input().split()))
#     print ["YES", "NO"][len(a1) >= k]