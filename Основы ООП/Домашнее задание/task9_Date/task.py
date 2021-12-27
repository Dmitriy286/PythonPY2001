# TODO class Date
class Date:
    def __init__(self, day: int, month: int, year: int):
        """
        Создаем дату
        :param day: день
        :param month: месяц
        :param year: год
        """
        self.day = None
        self.day_prove(day)
        self.month = month
        self.month = None
        self.month_prove(month)
        self.year = year
        self.year = None
        self.year_prove(year)

    def day_prove(self, day: int):
        if not isinstance(day, int):
            raise TypeError("Введено не целочисленное значение")
        self.day = day

    def month_prove(self, month: int):
        if not isinstance(month, int):
            raise TypeError("Введено не целочисленное значение")
        self.month = month

    def year_prove(self, year: int):
        if not isinstance(year, int):
            raise TypeError("Введено не целочисленное значение")
        self.year = year

    def __repr__(self) -> str:
        return f"Date({self.day}, {self.month}, {self.year})"

    def __str__(self) -> str:
        return f"{self.day:0>2}/{self.month:0>2}/{self.year}"


if __name__ == "__main__":
    date_1 = Date(1, 1, 2021)
    print(date_1)
    print([date_1])