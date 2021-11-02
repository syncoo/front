'''
if-else格式和作用
if 条件:
    满足条件执行的代码
else:
    不满足条件执行的代码

if判断条件,如果条件满足,执行if后的代码,如果条件不满足,执行else后面的代码
'''

def is_net(age):
    if age >= 18:
        print('可以上网')
    else:
        print('年龄不够,上什么网,滚去学习')

age = int(input('请输入你的年龄'))
is_net(age)