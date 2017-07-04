#Author:ithuplion
products_list=[
    ("iphone",5800),
    ("xiaomi",3600),
    ("watch",1200),
    ("meizu",5000),
]
shopping_list=[]
salary=input("please input your salary:")
if salary.isdigit():
    salary=int(salary)
    while True:
        for index,item in enumerate(products_list):
            # print(products_list.index(item)+1,item)
            print(index,item)
        user_choice=input("选择要买商品>>>:")
        if user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice<len(products_list) and user_choice>=0:
                p_item=products_list[user_choice]
                if p_item[1]<salary:
                    shopping_list.append(p_item)
                    salary-=p_item[1]
                    print("Added %s into shopping cart,your current balance is %s"%(p_item,salary))
                else:
                    print("你的余额只剩%s"%())
            else:
                print("product code %s is not exit!"% user_choice)
        elif user_choice == 'q':
           print("---------shopping list-----------------")
           for p in shopping_list:
               # print(p)
            print("Your current bablance",salary)
        else:
            print("invalid option")
        break