with open('names.txt', 'r') as file:
    names = file.read()

new_names = names.strip().split(' ')
new_names = [name.rstrip() for name in new_names if name != '']

print(new_names)
for offset in range(2):
    for name in new_names[offset::2]:
        print(name)
    print ('-------')
