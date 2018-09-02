def fileNaming(names):
    all_names = {}
    output = []
    for name in names:
        print(name, output)
        if name in all_names.keys():
            new_name = name + '(' + str(all_names[name]) +')'
            all_names[name] += 1
        else:
            new_name = name
            all_names[name] = 1

        if new_name in output:
            new_name += '(1)'

        output.append(new_name)
        print(all_names)
        print('**********')
    return output

# print(fileNaming(["doc",
#  "doc",
#  "image",
#  "doc(1)",
#  "doc"]))

print(fileNaming(["a(1)",
 "a(6)",
 "a",
 "a",
 "a",
 "a",
 "a",
 "a",
 "a",
 "a",
 "a",
 "a"]))