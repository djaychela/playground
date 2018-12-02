class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.area = height * width

    def __str__(self):
        return '{} x {} = {}'.format(self.height, self.width, self.area)

    ...


def primarySchool(height, width):
    return str(Rectangle(height, width))


print(primarySchool(34,2))