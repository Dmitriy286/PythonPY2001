# def func_1(a, b):
#     c = a + b
#     print(c)
#     return c
#
# def func_2(c, d):
#     e = c + d
#     print(e)
#
# if __name__ == "__main__":
#
#     # c = func_1(2, 3)
#     func_2(func_1(2, 3), 5)


# как реализовать что-то типа этого:
def linked_nodes(left_node: Node(*args), right_node: Optional["Node"] = None) -> None:

    return left_node(*args, right_node)
# т.е. не используя атрибуты класса создать ссылку на другую функцию

# или так:
def linked_nodes(*args):

    return args[0][1] == args[1]

def func_0(a, b):
    c = a + b
    return c

def func_3(*args):
    print(args[0][1])


if __name__ == "__main__":
    func = func_0(7, 8)
    func_3([9, func], 2)