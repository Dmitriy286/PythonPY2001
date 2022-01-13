# Придумать и написать 3 абстрактных класса,
# описывающих любой объект.
# Каждый класс следует оформлять в отдельном модуле.
# Например, в качестве объектов могут выступать материальные
# сущности стол, дерево, и даже нематериальные стек, Facebook.

# Для каждого класса выделить 3-5 характеристик и записать их в виде атрибутов
#
# Сформировать для каждого класса 3-5 методов, которые будет описывать
# возможные действия с объектом.
# Реализацию самих методов писать не нужно, достаточно только названия.



class IceCream:
    def __init__(self, weight: int, color: str, taste: str):
        """
        Создание и подготовка к использованию объекта "Мороженое"

        :param weight: вес мороженого
        :param color: цвет мороженого
        :param taste: вкус мороженого
        """
        self.weight = weight  # вес
        self.color = color  # цвет
        self.taste = taste  # вкус

    def is_ice(self) -> bool:
        """
        Функция, проверяющая, принят в работу лед со сливками или нет
        :return: Объект лед со сливками или нет
        """
        ...

    def establish_weight(self, weight: int) -> int:
        """
        Функция, которая определяет вес будущего мороженого.

        :param weight: вес мороженого
        :return: Вес мороженного в граммах
        """
        ...


if __name__ == "__main__":
    icecream = IceCream(125, "white", "vanilla")
