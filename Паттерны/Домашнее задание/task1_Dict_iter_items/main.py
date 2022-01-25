from typing import Iterator, Tuple, Hashable, Any, Dict


class MyDict(Dict):  # TODO Наследование от класса dict
    def __iter__(self):
        for i, j in zip(self.keys(), self.values()):
            yield i, j
        # TODO переопределить метод __iter__


if __name__ == "__main__":
    my_dict = MyDict({
        1: "a",
        2: "b",
        3: "c"
    })
    for key, value in my_dict:
        print(key, value)