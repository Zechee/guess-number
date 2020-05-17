import random

start = input('请选择一个起始数字: ')
end = input('请选择一个中止数字: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
	num = input('请输入数字: ')
	num = int(num)
	count = count + 1

	if num < r:
		print('猜错了，数字猜小了！')

	elif num > r:
		print('猜错了，数字猜大了！')

	else:
		print('恭喜你，猜对了！')
		print('你一共猜了', count, '次')
		break