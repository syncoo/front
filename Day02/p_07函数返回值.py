'''
return 返回一个函数的结果
格式:
    return 数据
一个函数,无论在哪遇到return,那么这个函数都会直接结束执行,回到调用处
return后面可以没有数据
函数也可以没有return,函数默认返回 None.
'''

def get_num():
    return 1

get_num()

print(get_num())

# 将一个函数返回值赋给一个变量
a = get_num()
print(a)

def show():
    print(1)
    print(2)
    return
    print(3)
    print(4)


a = show()
print(a)    # 在函数定义处, return后面写不写None,输出结果都会显示None
print('over')
