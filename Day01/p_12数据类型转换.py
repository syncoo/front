'''
int(x)  将x转换为一个整数
float(x) 将x转换成一个浮点数
str(x) 将x转换成一个字符串

ASCII码
48   0
65   A
97   a
'''
# 转换成整数类型
print(int(1))
print(int(1.1))
print(int('1'))
# print(int('1.1')) # 转换错误
# print(int('abc')) # 转换错误

# 转换成浮点类型
print(float(1))
print(float(1.1))
print(float('1.1'))
print(float('1'))
# print(float('abc')) # 转换错误

# 转换成字符串
print('|' + str(1) + '|')
print('|' + str(1.1) + '|')
print('|' + str('1') + '|')
print('|' + str('1.1') + '|')
print('|' + str('abc') + '|')
print('|' + str(True) + '|')

# chr函数
# 讲一个数字转换成字符
print(chr(48)) # '0'
print(chr(65)) # 'A'
print(chr(97)) # 'a'

# ord函数
# 讲一个数字转换成字符
print(ord('0')) # 48
print(ord('A')) # 65
print(ord('a')) # 97
