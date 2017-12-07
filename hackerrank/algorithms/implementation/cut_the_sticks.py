def cut_the_sticks(sticks_array):
    cut = True
    while cut:
        current_cut = min(sticks_array)
        for i in range(len(sticks_array)):
            sticks_array[i] -= current_cut
        print(len(sticks_array))
        while sticks_array.count(0):
            sticks_array.remove(0)
        if sum(sticks_array) == 0:
            cut = False


print(cut_the_sticks([5, 4, 4, 2, 2, 8]))
print(cut_the_sticks([1, 2, 3, 4, 3, 3, 2, 1]))
