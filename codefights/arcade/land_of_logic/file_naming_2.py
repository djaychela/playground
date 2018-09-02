def fileNaming(names):
    all_names = {}
    output = []
    for name in names:
        if name not in output:
            all_names[name] = True
            output.append(name)
        else:
            i=1
            present = True
            while present:
                new_name = name + '(' + str(i) + ')'
                if new_name not in output:
                    output.append(new_name)
                    present = False
                i+=1
        print(name, all_names.keys(), output)
    return output

print(fileNaming(["doc",
 "doc",
 "image",
 "doc(1)",
 "doc"]))
#
# print(fileNaming(["a(1)",
#  "a(6)",
#  "a",
#  "a",
#  "a",
#  "a",
#  "a",
#  "a",
#  "a",
#  "a",
#  "a",
#  "a"]))