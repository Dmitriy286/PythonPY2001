class Parent:
    CLS_PUB_ATTR: int = "71"
    __CLS_PRVT_ATTR: str = "2"
    _CLS_PRT_ATTR: dict = {3: 3}

    def __init__(self, slf_pub_attr, slf_prvt_attr, slf_prt_attr):
        """
        Конструктор экземпляра класса Parent
        :param slf_pub_attr: Публичный атрибут экземпляра'
        :param slf_prvt_attr: Приватный атрибут экземпляра
        :param slf_prt_attr: Защищенный атрибут экземпляра
        """
        self.slf_pub_attr = slf_pub_attr
        self.__slf_prvt_attr = slf_prvt_attr
        self._slf_prt_attr = slf_prt_attr

    @classmethod
    def is_valid(cls):
        if not isinstance(cls.CLS_PUB_ATTR, int):
            raise TypeError("Первый аргумент класса число")

    def slf_pub_meth(self, data):
        """
        Публичный метод экземпляра
        :param data:
        :return:
        """
        print(f"Это публичный метод экземпляра, печатаем переданные данные: {data}")

    def __slf_prvt_meth(self, data_1):
        """
        Приватный метод экземпляра. При вызове рэйзится ошибка.
        :param data_1:
        :return:
        """
        print(f"Это публичный метод экземпляра, печатаем переданные данные: {data_1}")

    def _slf_prt_meth(self, data_2):
        """
        Защищенный метод экземпляра. При вызове рэйзится ошибка, но можем читать.
        :param data_2:
        :return: data_2
        """

        return data_2

    @classmethod
    def cls_pub_meth(cls, arg_1):
        """
        Публичный метод класса.
        :param arg_1:
        :return: arg_1
        """
        return arg_1

    @classmethod
    def __cls_prvt_meth(cls):
        """
        Приватный метод класса. При вызове выдаст ошибку.
        :param arg_2:
        :return: None
        """

    @classmethod
    def _cls_prt_meth(cls, arg_2):
        """
        Защищенный метод класса. При вызове выдаст ошибку, но прочитать сможем.
        :param arg_2:
        :return: arg_2
        """
        return arg_2

    @staticmethod
    def stat_pub(stat_arg_1):
        """
        Публичный статический метод.
        :param stat_arg_1: принимаемый аргумент
        :return: stat_arg_1
        """

        return stat_arg_1

    @staticmethod
    def __stat_prvt():
        """
        Приватный статический метод. Ошибка при вызове.
        :return: None
        """

    @staticmethod
    def _stat_prt(stat_srg_2):
        """
        Защищенный статический метод. Ошибка при вызове, можем читать.
        :param stat_srg_2:
        :return: stat_arg_2
        """

        return stat_srg_2

class Child(Parent):

    def __init__(self, slf_pub_attr, slf_prvt_attr, slf_prt_attr):
        super().__init__(slf_pub_attr, slf_prvt_attr, slf_prt_attr)

    @classmethod
    def is_valid(cls):
        if not isinstance(cls.CLS_PUB_ATTR, int):
            raise TypeError("Первый аргумент класса число")

if __name__ == "__main__":
    cls_1 = Parent
    print(cls_1("arg_1", "arg_2", "arg_3"))

    cls_child_1 = Child(1, 2, 3)
    print(cls_child_1.CLS_PUB_ATTR)
    cls_child_1.CLS_PUB_ATTR = 56
    print(cls_child_1.CLS_PUB_ATTR)
    cls_child_1.CLS_PUB_ATTR = "56"
    print(cls_child_1.CLS_PUB_ATTR)


#fixme что значит проверить атрибуты и методы родительского класса?

#fixme почему не работает is_valid?