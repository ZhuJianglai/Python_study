# -*- coding: utf-8 -*-
# @Time    : 2019-1-7 19:17
# @Author  : 081191
# @FileName: re模块.py
# @Software: PyCharm


#re模块，常用的正则表达匹配

import re
strA='hfjqfkdsha hah121fs fakjshoua fsdjahf hjash123'
res=re.match("^h\d+",strA)
print(res.group())


#  '.' 默认匹配任意字符除了换行符\n
#  '^' 匹配字符开头，re.macth（）不是用，re.searrch()
#  '$' 匹配字符结尾
#  '*' 匹配前一个字符0次或多次
#  '+' 匹配前字符1次或多次
#  '?' 匹配前一个字符1次或0次
#  '{m}'匹配前一个字符m次
#  '{n,m}' 匹配前一个字符n到m次
#  '\A' 只从字符开头匹配
#  '\z'匹配字符结尾
#  '\d\匹配数字
#  '\D'匹配非数字
#  '\w' 匹配【A-Z a-z 0-9]
#  '\W' 匹配非【A-Z a-z 0-9]
# 分组匹配语法
re.search("?p<name>[0-9]+","112312fdsfa")
#常用语法
re.match()
re.findall()
re.search()
re.split()#分割
re.sub()# 替换