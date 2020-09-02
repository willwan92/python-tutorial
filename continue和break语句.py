# break语句：
# break语句用在while和for循环中，用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。
# 如果您使用嵌套循环，break语句将停止执行最深层的循环

var = 10
while var > 0:              
	print('当前变量值 :', var)
	var = var -1
	if var == 5:   # 当变量 var 等于 5 时退出循环
		break

# continue语句：
# continue语句用在while和for循环中，跳出本次循环，然后继续进行下一轮循环，而break跳出整个循环。

num = 10
while num > 0:
	num -= 1
	if (num == 5): continue
	print('当前变量num值：', num)
