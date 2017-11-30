def save_the_prisoner(num_of_prisoners, num_of_sweets, start_prisoner_id):
    current_prisoner = start_prisoner_id
    while num_of_sweets > 1:
        num_of_sweets-= 1
        current_prisoner += 1
        if current_prisoner > num_of_prisoners:
            current_prisoner = 1
    return current_prisoner


print(save_the_prisoner(5,2,1))
print(save_the_prisoner(5,2,2))