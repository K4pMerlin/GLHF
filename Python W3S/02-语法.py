#用井号键表示注释
if 5>2:
    print("indeed")
#至少需要一个空格
if 5 > 2:
 print("Five is greater than two!")  
if 5 > 2:
        print("Five is greater than two!")

#这里的缩进很重要,表示一个个的"代码块",接下来写一些出错的东西

#没有空格
"""
if 5 > 2:
print("Five is greater than two!")
"""

#没有相同的空格数量
"""
if 5 > 2:
 print("Five is greater than two!") 
        print("Five is greater than two!")
"""