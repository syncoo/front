'''
if 条件1:
    满足条件1执行的代码
elif 条件2:
    满足条件2执行的代码
elif 条件3:
    满足条件3执行的代码
...
else:
    不满足条件执行的代码

顺序判断,先判断条件1,满足条件,执行条件1后面的代码;
如果不满足条件1,那么继续判断条件2,如果满足执行条件2后面的代码;
如果不满足条件2,继续向后判断,满足哪个条件,执行哪个条件后的代码.

else是指如果所有前面的条件都不满足,那么执行else后面的代码
else是一个可选的模块,可以省略不写,但是一般会写,用来容错
'''

# if_elif_else格式
def is_weekday(day):
    if day == '1' or day == '一':
        print('Monday')
    elif day == '2' or day == '二':
        print('Tuesday')
    elif day == '3' or day == '三':
        print('Wednesday')
    elif day == '4' or day == '四':
        print('Thursday')
    elif day == '5' or day == '五':
        print('Friday')
    elif day == '6' or day == '六':
        print('Saturday')
    elif day == '7' or day == '日':
        print('Sunday')
    else:
        print('You can only input 1~7')

d = input('Input:')
is_weekday(d)