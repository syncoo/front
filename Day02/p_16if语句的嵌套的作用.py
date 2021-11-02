'''
if条件:
    if条件:
        if条件:
        ...
'''
# 定义一个函数,用来判断成绩的优良中差不及格

def is_score_level(score):
    # 先判断输入的成绩是否有效
    if score >= 0 and score <= 100:
    # 成绩有效,判断级别
        if score >= 90:
            print(f'得分: {score } , 级别优')
        elif score >= 80:
            print(f'得分: {score } , 级别良')
        elif score >= 70:
            print(f'得分: {score } , 级别中')
        elif score >= 60:
            print(f'得分: {score } , 级别差')
        else:
            print(f'得分{score }, 级别 不及格')
    else:
        print(f'输入的成绩无效!')

a = int(input('请输入分数:'))
is_score_level(a)