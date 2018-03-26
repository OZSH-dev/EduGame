

class Entity:
    entities = set()

    def __init__(self):
        self.entities.add(self)
        self.__coordinates = (0, 0)
        self.actions = set()

    @property
    def x(self):
        return self.__coordinates[0]

    @property
    def y(self):
        return self.__coordinates[1]

    @x.setter
    def x(self, value):
        self.__coordinates = (value, self.__coordinates[1])

    @y.setter
    def y(self, value):
        self.__coordinates = (self.__coordinates[0], value)

    def tick(self):
        for action in self.actions:
            action()


