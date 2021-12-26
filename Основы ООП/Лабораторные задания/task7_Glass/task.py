from typing import Union

class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Создаем объект стакан

        :param capacity_volume: объем стакана
        :param occupied_volume: объем жидкости
        """

        self.capacity_volume = None
        self.capacity_volume_init(capacity_volume)

        self.occupied_volume = None
        self.occupied_volume_init(occupied_volume)

    def capacity_volume_init(self, capacity_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Not an int or float")
        if capacity_volume <= 0:
            raise ValueError("Not a positive number")
        self.capacity_volume = capacity_volume

    def occupied_volume_init(self, occupied_volume: Union[int, float]):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Not an int or float")
        if occupied_volume < 0:
            raise ValueError("Less than zero")
        self.occupied_volume = occupied_volume


# TODO  создать класс Glass


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
