class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        if year % 4 == 0:
            return True
        else:
            return False# TODO записать условие проверки високосного года

    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.is_leap_year(year):
            return self.DAY_OF_MONTH[1][month - 1]
        else:
            return self.DAY_OF_MONTH[0][month - 1]# TODO вернуть количество дней указанного месяца

    def is_valid_date(self, day: int, month: int, year: int) -> None:
        """Проверяет, является ли дата корректной"""
        if day > self.get_max_day(month, year):
            raise ValueError("???")# TODO если указанный набор день, месяц и год неверны, то вызвать ошибку ValueError

    # TODO записать getter и setter для дня
    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        if not isinstance(day, int):
            raise TypeError("Введено не число")

        if not 0 < day <= 31:
            raise ValueError("Выходит за границы диапазона 1 - 31")

        self._day = day

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError("Введено не число")

        if not 0 < month <= 12:
            raise ValueError("Выходит за границы диапазона 1 - 12")

        self._month = month

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError("Введено не число")

        if year < 0:
            raise ValueError("Введено число меньше 0")

        self._year = year

    # TODO записать getter и setter для месяца

    # TODO записать getter и setter для года

    def __str__(self):
        return f"{self.__class__.__name__} ({self.day:<2}, {self.month:<2}, {self.year:<4})"

if __name__ == "__main__":
    date_1 = Date(29, 2, 2021)
    print(date_1)