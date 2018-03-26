from entities.logic.base.entity import Entity


class Dinosaur(Entity):
    def __init__(self):
        super().__init__()

        self.run_ticks = 0
        self.is_jumping = False
        self.is_dead = False
        self.geometry = (45, 45)
        self.actions.add(self.count_run_ticks)
        self.floor = 0

        self.gravity = -0.05
        self.jump_time = 0
        self.init_jump_velocity = 0
        self.actions.add(self.handle_jump)
        self.actions.add(self.handle_move)

    def count_run_ticks(self):
        self.run_ticks += 1

    def handle_jump(self):
        if self.is_jumping:
            self.jump_time += 0.01
            next_y = self.y - self.init_jump_velocity * self.jump_time
            if next_y > self.floor:
                self.y = self.floor
                self.is_jumping = False
                return
            self.y = next_y
            self.init_jump_velocity += self.gravity * self.jump_time

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.init_jump_velocity = 3.5
            self.jump_time = 0

    def handle_move(self):
        for entity in self.entities:
            if entity == self:
                continue
            if entity.x <= self.x + self.geometry[0] and entity.x > self.x:
                if entity.y <= self.y:
                    self.is_dead = True
