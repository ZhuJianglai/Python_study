# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-



#---------------
#启动程序后，让用户输入工资，然后打印商品列表
#允许用户根据商品编号购买商品
#用户选择后，检测余额是否够，够就直接扣款，不够提醒
#可随时退出，退出时，打印已购买商品喝余额


product_list=[
    ('iphone',5800),
    ('Mac Pro',9800),
    ('bike',1200),
    ('Watch',10600),
    ('Coffice',31),
    ('office',301),
    ('car',30100),
    ('book',100),
]
shopping_list=[]
salary = input("请输入你的金额>>>:")
if salary.isdigit():
    salary=int(salary)
    # print(salary)
    while True:
        # for item in product_list:
        #     print(product_list.index(item),item)
        for index,item in enumerate(product_list):
            print(index,item)
        user_chose=input("选择要买啥？>>>:")
        if user_chose.isdigit():
            user_chose=int(user_chose)
            if user_chose>=0 and user_chose<len(product_list):
                if salary>product_list[user_chose][1]:
                    salary -=product_list[user_chose][1]
                    shopping_list.append(product_list[user_chose])
                    print("您的余额：{_salary}".format(_salary=salary))
                    print(shopping_list)
                else:
                    print("您的余额不足")
            else:
                print("您输入的商品不存在！")
        elif user_chose=='q':
            print("您的余额为%d"%salary)
            for i in shopping_list:
                print(i)
            exit()
        else:
            print("您输入的商品不存在！")
else:
    print("您输入的金额无效!")


