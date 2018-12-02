def masterVsFighters(fighters, master):
    fighter_attribs = {'a': [5, 6, 2],
                       'b': [6, 8, 2],
                       'g': [8, 6, 5]}
    fighters_defeated = 0
    hits_by_fighters = 0
    hits_by_master = 0
    damage_by_fighters = 0
    damage_by_master = 0
    master_defeated = False
    for fighter in fighters:
        current_fighter = fighter_attribs[fighter].copy()
        print('start of fight:')
        print(master, current_fighter)
        while current_fighter[0] > 0:
            # fighter attacks master
            this_damage_by_fighter = (current_fighter[1] - master[2])
            print(this_damage_by_fighter)
            master[0] -= this_damage_by_fighter
            damage_by_fighters += this_damage_by_fighter
            hits_by_fighters += 1
            # check for defeat of master
            if master[0] <= 0:
                master_defeated = True
                break
            # master attacks fighter
            this_damage_by_master = (master[1] - current_fighter[2])
            current_fighter[0] -= this_damage_by_master
            damage_by_master += this_damage_by_master
            hits_by_master += 1

            print(master, current_fighter)
        if master[0] > 0:
            print('master wins!')
            fighters_defeated += 1
        if current_fighter[0] >= 0:
            print('fighter wins!')
        print('next')

    if hits_by_fighters > 0:
        avg_damage_by_fighters = f'{damage_by_fighters / hits_by_fighters:.2f}'
    else:
        avg_damage_by_fighters = '0.00'
    if hits_by_master > 0:
        avg_damage_by_master = f'{damage_by_master/ hits_by_master:.2f}'
    else:
        avg_damage_by_master = '0.00'

    print(f'winner {"Master" if not master_defeated else "Fighters"}')
    print(f'fighters defeated: {fighters_defeated}')
    print(f'fighters remain: {len(fighters) - fighters_defeated}')
    print(f'masters health: {max(master[0], 0)}')
    print(f'hits by fighters: {hits_by_fighters}')
    print(f'hits by master: {hits_by_master}')
    print(f'damage by fighters: {avg_damage_by_fighters}')
    print(f'damage by master: {avg_damage_by_master}')

    return [("Master" if not master_defeated else "Fighters"), str(fighters_defeated),
            str(len(fighters) - fighters_defeated), str(max(master[0], 0)), str(hits_by_fighters),
            str(hits_by_master), avg_damage_by_fighters, avg_damage_by_master]

    return


# fighters = ["a", "a", "b"]
# master = [14, 6, 4]

# fighters = ["a", "a", "a", "b", "g"]
# master= [7, 10, 5]
# Expected_Output= ["Fighters", "4", "1", "0", "5", "4", "1.40", "8.00"]

# fighters = ["g", "g", "g"]
# master = [18, 6, 5]
# expected_output = ["Fighters", "2", "1", "0", "18", "17", "1.00", "1.00"]
#
# fighters = ["b"]
# master = [1, 6, 1]
# expected_output = ["Fighters", "0", "1", "0", "1", "0", "7.00", "0.00"]
#
#
fighters = ['a','a','a','a']
master = [20, 10, 5]
print(masterVsFighters(fighters, master))
