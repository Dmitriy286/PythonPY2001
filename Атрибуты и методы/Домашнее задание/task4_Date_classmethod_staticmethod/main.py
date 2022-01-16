class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

        # self.max_day = None
        # self.get_max_day(self.month, self.year)

    @staticmethod
    def is_leap_year(year: int):
        """Проверяет, является ли год високосным"""
        if year % 4 == 0:
            return True
        else:
            return False  # TODO

        # if year % 4 == 0:
        #     return self.DAY_OF_MONTH[1]
        # else:
        #     return self.DAY_OF_MONTH[0]

    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.is_leap_year(year) is False:
            return self.DAY_OF_MONTH[0][month - 1]
        else:
            return self.DAY_OF_MONTH[1][month - 1]

        # TODO

    # @classmethod # classmethod т.к. он одинаков для всех лет. Любой год будет проходить такую проверку.
    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""

        if not isinstance(day, int):
            raise TypeError("Вы ввели не число")

        if day <= 0:
            raise ValueError("Вы ввели отрицательное число")

        if day > self.get_max_day(month, year):
            raise ValueError("В текущем месяце меньше дней")

        if not isinstance(month, int):
            raise TypeError("Вы ввели не число")

        if month <= 0:
            raise ValueError("Вы ввели отрицательное число")# TODO

        if not isinstance(year, int):
            raise TypeError("Вы ввели не число")

        if year  <= 0:
            raise ValueError("Вы ввели отрицательное число")

        if len(str(year)) != 4:
            raise ValueError("Введите цифру года из четырех цифр")

    def __repr__(self) -> str:
        return f"{self.day}, {self.month}, {self.year}"



if __name__ == "__main__":
    # day = int(input("Insert day: "))
    # month = int(input("Insert month: "))
    # year = int(input("Insert year: "))

    day_ = 25
    month_: int = 2
    year_ = 2021

    date_1 = Date(day_, month_, year_)
    print(repr(date_1.get_max_day))
    print(date_1.is_leap_year)
    print(date_1.get_max_day(month_, year_))
    print(date_1.is_leap_year(year_))
    print(date_1)
    print(date_1.DAY_OF_MONTH[0][1])
    print(date_1.DAY_OF_MONTH[1][1])

