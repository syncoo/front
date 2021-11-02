'''
if语句的格式:
if 条件:
    满足条件执行的代码
'''

def is_net(age):
    if age >= 18:
        print('可以上网')


age = int(input('请输入你的年龄'))
is_net(age)