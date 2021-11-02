'''
一个函数中可以存在多个Return.
但是,只能有一个语句有效
在执行顺序上,第一个遇到的return有效
'''

def get_num():
    return 1
    return 2    # 可以写,但是不执行
    return 3    # 可以写,但是不执行

print(get_num())