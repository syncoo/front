'''
函数说明文档
DocString
可写可不写
'''

def show():
    '''
    这是show函数的说明文档
    show 函数的作用是用来显示一个字符串
    '''
    print('Hello, World')

show()

help(show)  # help()函数可以调用上面函数的函数说明文档
help(print) # 按住Ctrl点击 print,可以查看print函数的定义文件