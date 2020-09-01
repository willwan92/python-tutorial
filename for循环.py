# 迭代字符串
for letter in 'Python':
	print('当前字母 :', letter)

# 迭代列表
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:
	print('当前水果 :', fruit)
 
# 通过序列索引迭代
for index in range(len(fruits)):
	print('当前水果 :', fruits[index])

# 循环使用 else 语句
# for … else语句：else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
for num in range(10,20):  # 迭代 10 到 20 之间的数字
	for i in range(2,num): # 根据因子迭代
		if num%i == 0:      # 确定第一个因子
			j=num/i          # 计算第二个因子
			print('%d 等于 %d * %d' % (num,i,j))
			break            # 跳出当前循环
	else:                  # 循环的 else 部分
		print(num, '是一个质数')

print("Good bye!")