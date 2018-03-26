from .base.entity_bridge import EntityBridge
from .logic.dinosaur import Dinosaur as Dino
from .logic.cactus import Cactus as Plant


class Dinosaur(EntityBridge):
    def __init__(self, parent):
        super().__init__(Dino, "assets/dinosaur.png", parent)


class Cactus(EntityBridge):
    def __init__(self, parent):
        super().__init__(Plant, "assets/cactus.png", parent)