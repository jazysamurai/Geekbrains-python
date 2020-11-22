# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение
# светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.

from time import sleep
from itertools import cycle
class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        for counter, value, in enumerate(cycle(TrafficLight.__color)):
            if value == 'red':
                sleep(7)
                print(value)
            if value == 'yellow':
                sleep(2)
                print(value)
            if value == 'green':
                sleep(4)
                print(value)
            if counter > 10:
                break

TrafficLight = TrafficLight()
TrafficLight.running()
