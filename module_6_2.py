class Vehicle:

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color if color.lower() in [c.lower() for c in Vehicle.__COLOR_VARIANTS] else 'unknown'

    def get_model(self) -> str:
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        if new_color.lower() in [c.lower() for c in Vehicle.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        super().__init__(owner, model, engine_power, color)

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()