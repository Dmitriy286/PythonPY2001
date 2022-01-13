class Test:
    """
    Documentation
    """
    class_atr = "test_atr"

    def __init__(self, arg):
        ...
        self.arg = arg
        self.arg_2 = None
        self.arg_2_init()

        cls = self.__class__
        print(cls.class_atr)

    def arg_2_init(self):
        self.arg_2 = 500

    def print_arg_2(self):
        print(self.arg_2)


if __name__ == "__main__":
    test_1 = Test(1)
    print(test_1.__class__)
    print(test_1.__dict__)

    print(dir(test_1))

    test_1.print_arg_2()
    test_2 = Test(2)
    test_2.new_arg = "test"
    print(test_2.__dict__)

    print(type(test_1))
    print(test_1.__class__)
    print(type(test_1) is test_1.__class__)
    print(type(test_1) is test_2.__class__)

    test_2.print_arg_2()

    Test.print_arg_2(test_2)
    print(type(test_2.print_arg_2))
    print(type(Test.print_arg_2))

    print(Test.__name__)
    print(Test.__module__)
    print(Test.__doc__)
    print(Test.class_atr)

    print(Test.__dict__)
    print(test_1.__dict__)


class Glass:
    class_atrib = "test 2"
    count = 0

    def __init__(self):
        print(self.__dict__)
        self.count = self.count + 1
        print(self.__dict__)

        # cls = self.__class__
        # cls = type(self)
        # cls.count += 1
        type(self).count += 1



    def __repr__(self):
        return f"{self.__class__.__name__}()"

glass = Glass()
print(repr(glass))

print("-------------")
print(Glass.__dict__)
print(glass.count)
print(Glass.count)
print("-------------")
glass_1 = Glass()
print(glass_1.count)
print(Glass.count)
print("-------------")
print(Glass.count)
glass_2 = Glass()
print(glass_2.count)

# class Glassqwerty:
#     def __repr__(self):
#         return f"{self.__class__.__name__}()"
#
# glass = Glassqwerty()
# print(repr(glass))

class Glass2:
    material = "paper"

    @classmethod
    def set_material(cls, material):
        cls.material = material

    def __str__(self):
        return f"Стакан из материала - {self.__class__.material}"

    def return_list(self):
        return [1, 2, 3]

    def __len__(self):
        print("Вызван метод \"__len__\"")
        return self.len

glass_3 = Glass2()
glass_4 = Glass2()

print(glass_3)
print(glass_4)

Glass2.set_material("Glass")

print(glass_3)
print(glass_4)

DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )


def is_leap_year(year: int):

    if year % 4 == 0:
        return DAY_OF_MONTH[1]
    else:
        return DAY_OF_MONTH[0]

print(is_leap_year(2020)[1])
print("-------------------------: 1")


def qq():
    a = 1
    b = 2
    print(a)
    return b
qq()
# print(qq())
q = qq()
print("-------------------------: 2")
print(q)
print("-------------------------")
print(qq)
print("-------------------------")
print(qq())
print("-------------------------")
