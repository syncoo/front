'''
输出的基本使用:
print()
输出-格式化操作符的使用
    1)占位符形式: 'a的值是%d' %值
    2)f-string: f'字符串 {数据}'
'''

# 占位符形式
# 情况1
a = 10
print('现在要打印一个数字,值是%d' % a)

# 情况2:多个值要用括号括起来
print('name: %s age: %d' % ('Tom', 12))

'''
常用占位符:
    %d  以整数输出
        %3d  输出时,数据占3个字符宽度 
        %03d 输出时,数据占3个字符宽度 ,当数字不足三个字符时,前缀补0  001
        %-3d 输出时,数据占3个字符宽度 , 左对齐
    %f  以小数输出
        %.3f 小数点后保留位数是3位
    %s  以字符串输出
'''
print('%d' % 1)
print('%5d' % 1)
print('%-5d' % 1)
print('%05d' % 1)
print('%5d' % 12345678) # 超出宽度,原样打印

print('π的值是%.2f' % 3.1415926)
print('π的值是%.2f' % 3.1) # 小数位数不够,后面补零

# f'string' 格式化字符串
name = "Tom"
age = 12
print(f'name:{name} age:{age} score:{99}')

print(f'Name:{"Jerry"} Age:{True} Score:{99}')

s = f'name:{name} age:{age} score:{88}' # 我们也可以把格式化后的字符串复制给某个变量名
print(s)
