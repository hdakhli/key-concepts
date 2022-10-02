from engine import Engine


class Vehicle:
    def __init__(self, color: str, tires: int, engine: Engine):
        self._color = color
        self._tires = tires
        self._engine = engine

    def go_to(self, x: float, y: float):
        print(f"I'm moving to {x, y}")

    def brake(self):
        print("I'm braking...")

    def start(self):
        print("I'm starting...")


class Tractor(Vehicle):
    def __init__(self, color: str, tires: int, engine: Engine, doors: int):
        super().__init__(color, tires, engine)
        self._doors = doors


tractor = Tractor("red", 4, Engine(), 2)
tractor.start()


