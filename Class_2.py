class TelegramBot:
    def __init__(self, menu_1: str, menu_2: str):
        """
        Создание телеграм-бота

        :param menu_1: первый пункт меню бота
        :param menu_2: второй пункт меню бота
        """
        self.menu_1 = menu_1
        self.menu_2 = menu_2


    def welcome_message(self, message_1: str) -> str:
        """
        Функция, устанавливающая приветственное сообщение пользователю

        :param message_1: текст сообщения
        :return: текст сообщения, которое видит пользователь
        """
        ...


    def max_message_amount(self, amount: int) -> int:
        """
        Функция, устанавливающая максимальное количество сообщений,
        которые может отправить пользователь боту

        :param amount: количество сообщений
        :return: количество сообщений
        """
        ...


    def bye_message(self, message_2: str) -> str:
        """
        Функция, устанавливающая прощальное сообщение пользователю

        :param message_1: текст сообщения
        :return: текст сообщения, которое видит пользователь
        """
        ...


if __name__ == "__main__":
    Bot_1 = TelegramBot("Кнопка 1", "Кнопка_2")
