from math import pow

# 水仙花数
'''
水仙花数是指一个3位数，它的每个位上的数字的3次幂之和等于它本身
'''


def shui_xian_hua():
	num = int(input('请输入一个三整数：'))
	add_num = pow(num // 100, 3) + pow(num % 100 // 10, 3) + pow(num % 100 % 10, 3)
	if add_num == num:
		print('%d是水仙花数' % num)
	else:
		print('%d不是水仙花数' % num)


# 完美数
'''
一个数所以真因子（除了自身以外的约数）之和等于本身
'''


def wan_mei_shu():
	num = int(input('请输入一个整数：'))
	sum = 0
	for i in range(1, num):
		if num % i == 0:
			sum += i
	if num == sum:
		print('%d是完美数' % num)
	else:
		print('%d不是完美数' % num)


# 百钱白鸡
'''
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何
'''


def bai_qian_bai_ji():
	for i in range(4):
		gongji = 4 * i
		muji = 25 - 7 * i
		jichu = 3 * i + 75
		print('百钱可以买%d只公鸡，%d只母鸡，%d只鸡雏' % (gongji, muji, jichu))


# 菲波那切数列
'''
1,1,2,3,5,。。。后面数为前面两数之和
'''


def fibonacci_sequence():
	num = int(input('请输入要生成的范围，一个整数：'))
	f, b = 1, 1
	while f < num:
		print(f, end=' ')
		f, b = b, f + b


if __name__ == '__main__':
	# shui_xian_hua()
	# wan_mei_shu()
	# bai_qian_bai_ji()
	fibonacci_sequence()
