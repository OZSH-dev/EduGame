from entities.logic.base.entity import Entity


class Cactus(Entity):
    def __init__(self):
        super().__init__()
        self.speed = 1
        self.geometry = (30, 45)
        self.actions.add(self.move)

    def move(self):
        self.x -= 1
