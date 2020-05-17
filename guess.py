import random
r = random.randint(1, 100)
count = 0

while True:
	num = input('请输入数字(范围1-100): ')
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