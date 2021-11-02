'''
练习:
定义一个函数,
接受一个数字,判断该数字是否是偶数
'''
# 定义一个函数潘丹是否是偶数
def is_even(n):
    if n % 2 == 0:
        print(f'{n} 是偶数')
    else:
        print(f'{n} 是基数')

m = int(input('请输入一个数字'))
is_even(m)