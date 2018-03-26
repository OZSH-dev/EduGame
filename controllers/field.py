from entities.entities import Dinosaur, Cactus, EntityBridge
import random


class Field:
    def __init__(self, width, height, parent=None, old_field=None):
        self.parent = parent
        self.field_width = width
        self.field_height = height

        if old_field:
            self.best_result = old_field.best_result
            for entity in set(EntityBridge.entities):
                entity.delete()

        self.road_height = 300
        self.dinosaur_start_point = 100

        self.dinosaur = Dinosaur(parent)
        self.dinosaur.y = self.road_height
        self.dinosaur.x = self.dinosaur_start_point
        self.dinosaur.entity_logic_object.floor = 300
        self.cacti = set()
        self.cacti_cooldown = 0
        self.best_result = 0

    def handle_cacti(self):
        if random.randint(0, 100) == 42 and len(self.cacti) < 6 and self.cacti_cooldown == 0:
            cactus = Cactus(self.parent)
            cactus.y = self.road_height
            cactus.x = self.field_width
            self.cacti.add(cactus)
            self.cacti_cooldown = 200
        elif self.cacti_cooldown > 0:
            self.cacti_cooldown -= 1
        for cactus in set(self.cacti):
            if cactus.x == 0:
                self.cacti.remove(cactus)
                cactus.delete()

    def tick(self):
        self.handle_cacti()
        for entity in set(EntityBridge.entities):
            if self.dinosaur.entity_logic_object.is_dead:
                self.parent.restart_game()
            entity.tick()
