'''
实际参数: 传递的数据,函数调用时,括号中出现的数据
形式参数: 是在函数被调用时,接收函数调用传输过来的实参数据
实参和形参在传递时一一对应
'''

# 定义一个函数
def say_hi(name): # name就是形参
    print('hello',name)

# say_hi('Tom') # 'Tom'就是实参
# say_hi('Jack')
# say_hi('Rose')

def my_sum(a, b):
    print(a + b)

my_sum(1,2)
# my_sum(1) TypeError: my_sum() missing 1 required positional argument: 'b'
# my_sum(1,2,3)   TypeError: my_sum() takes 2 positional arguments but 3 were given