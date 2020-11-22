# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self):
        self._1sqm_mass = 45
        self._thickness = 2
        mass = self._length * self._width * self._1sqm_mass * self._thickness
        print(f'Road mass is: {mass} kilos')

road = Road(int(input('Input road length: ')), int(input('Input road width: ')))
print(road.mass_calc())

# Почему в выводе на консоли ещё и None - не понел
