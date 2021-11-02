'''
返回值 练习
需求:
    封装一个函数
    从键盘获取一个数字
'''

def get_num():
    k = input('请输入一个数字')
    k = int(k)
    return k

print(get_num() // 2)

'''
定义一个函数,传入两参数,并计算参数累加和返回
'''
def my_sum(a,b):
    # 当有参数后,不需要对参数重新从键盘进行输入新数据
    # a = 1
    # b = 2
    return a + b

s = my_sum(1,2)
print(s)
