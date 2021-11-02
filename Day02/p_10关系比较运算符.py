'''
比较运算符
运算符                     描述
==          检查两个操作数的值是否相等,如果是,则条件变为真
!=          检查两个操作数的值是否相等,如果不相等,则条件变为真
>           检查左操作数的值是否大于右操作数的值,如果是,则条件成立
<           检查左操作数的值是否小于右操作数的值,如果是,则条件成立
>=          检查左操作数的值是否大于或等于右操作数的值,如果是,则条件成立
<=          检查左操作数的值是否小于或等于右操作数的值,如果是,则条件成立

关系运算符的结果是bool类型
'''

def test_func():
    # ==
    print(1 == 2)   # False
    print(1 == 1)   # True

    print('*' * 10)
    # !=
    print(1 != 2)   # True
    print(1 != 1)   # False

    print('*' * 10)
    # >
    print(1 > 2)    # False
    print(2 > 1)    # True

    print('*' * 10)
    # <
    print(1 < 2)    # True
    print(2 < 1)    # False

    print('*' * 10)
    # >=
    print(1 >= 2)  # False
    print(2 >= 1)  # True

    print('*' * 10)
    # <=
    print(1 <= 2)  # True
    print(2 <= 1)  # False

test_func()