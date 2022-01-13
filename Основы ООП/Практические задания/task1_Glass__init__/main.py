from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Введено не число")
        if capacity_volume <= 0:
            raise ValueError("Введено отрицательное число")
        self.capacity_volume = capacity_volume

        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    Glass1 = Glass(200, 100)
    Glass2 = Glass(500, 499.9)

    print(Glass1)
    print(Glass2)

    # TODO попробовать инициализировать не корректные объекты
