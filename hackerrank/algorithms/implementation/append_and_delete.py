def append_and_delete(string1, string2, ops):
    compare = min(len(string1), len(string2))
    difference_letters = 0
    for i in range(compare):
        print(string1[i], string2[i], string1[i] == string2[i])
        if not string1[i] == string2[i]:
            difference_letters = i
            break
    needed = (len(string1) - difference_letters) + (len(string2) - difference_letters)
    if needed <= ops:
        return 'Yes'
    return 'No'


print(append_and_delete("hackerhappy", "hackerrank", 9))
print(append_and_delete('aba','aba',7))
