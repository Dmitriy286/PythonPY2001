class GasStation:
    def __init__(self, petroleum_type: str, number_of_cars: int):
        """
        Создает автозаправочную станцию

        :param petroleum_type: тип топлива
        :param number_of_cars: количество автомобилей
        """
        self.petroleum_type = petroleum_type
        self.number_of_cars = number_of_cars

    def petroleum_amount(self, amount: int) -> dict:
        """
        Функция, определяющая количество каждого типа топлива

        :param amount: количество топлива
        :return: словарь, в котором содержится информация по количеству каждого типа топлива
        """
        ...

    def car_types(self, type_: str) -> dict:
        """
        Функция, определяющая, какому количеству автомобилей требуется какое количество топлива

        :param type_: тип автомобиля
        :return: словарь с указанием типа автомобиля, потребляемого топлива и его количества
        """
        ...

    def queue(self, petroleum_amount: dict, car_types: dict) -> list:
        """
        Функция, формирующая очередь автомобилей на автозаправочной станции

        :param petroleum_amount: Функция, определяющая количество каждого типа топлива
        :param car_types: Функция, определяющая, какому количеству автомобилей требуется какое количество топлива
        :return: список, обозначающий очередь автомобилей на АЗС
        """
        ...


if __name__ == "__main__":
    Station_1 = GasStation("Солярка", 50)
