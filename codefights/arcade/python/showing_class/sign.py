class Functions(object):
    def __init__(self, value):
        self.value = value

    def sign(self):
        if self > 0:
            return 1
        elif self.value < 0:
            return -1
        else:
            return 0


def sign(x):
    return Functions.sign(x)



print(Functions.sign(34))