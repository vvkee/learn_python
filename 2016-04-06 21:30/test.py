#1 /usr/bin/env python
# -*- coding: utf-8 -*-

# 输入的字符转化为浮点型
number = raw_input('请输入数量：')

try:
    number = float(number)
    pass
except Exception as e:
    print('您输入的不是数字')
    raise

price = raw_input('请输入单价：')

# 输入的字符转化为浮点型
try:
    price = float(price)
    pass
except Exception as e:
    print('您输入的不是数字')
    raise

# 输出总价
print '总价为：' + str(number * price)
