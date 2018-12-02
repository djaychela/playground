def sortCodesignalUsers(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))


class CodeSignalUser:
    def __init__(self, name, _id, score):
        self.name = name
        self.id = _id
        self.score = score

    def __lt__(self, other):
        if int(self.score) < int(other.score):
            return True
        elif int(self.score) == int(other.score):
            print(f'equal {self.name}, {other.name}')
            return int(self.id) > int(other.id)
        return False


    def __repr__(self):
        return self.name

users = [["warrior", "1", "1050"],
         ["Ninja!", "21", "995"],
         ["recruit", "3", "995"]]


# c = CodeSignalUser("warrior", "1", "1050")
print(sortCodesignalUsers(users))
