'''
    运算符        逻辑表达式                     描述                                                 实例
    and          x and y        布尔"与",如果x为 False, x and y返回 False,否则它返回y的值             True and True,返回 True
    or           x or y         布尔"或",如果x是 True,它返回 True,否则它返回y的值                     False or True,返回 True
    not          not x          布尔"非",如果x为 True,返回 False.如果 x为 False,它返回 True          not True 返回 False, not False 返回 True

    逻辑运算符运算结果也是bool类型值.
'''

def test_func():
    # 逻辑与and, 可以理解为乘法, True为1, False为0
    print (True and True)   # True
    print (True and False)  # False
    print (False and True)   # False
    print (False and False)   # False

    print('*' * 10)
    # 逻辑或and, 可以理解为加法, True为1, False为0
    print(True or True)  # True
    print(True or False)  # True
    print(False or True)  # True
    print(False or False)  # False

    print('*' * 10)
    # 逻辑非not, 可以理解为加法, True为1, False为0
    print(not True)  # False
    print(not False)  # True

    print('*' * 10)
    a = int(input("number:"))
    print(a > 0 and a > 10) # and 逻辑运算

    print('*' * 10)
    print(1 and 2 and 3)    # 结果为3,把最后一个作为结果
    print(0 and 2 and 3)    # 结果为0,第一个已经为0了

    print(1 or 2 or 3)  # 结果为1
    print(0 or 2 or 3)  # 结果为2
    print(0 or 0 or 3)  # 结果为3
test_func()