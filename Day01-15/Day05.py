import random
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


# craps赌博游戏
'''
玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；如果点数和为2、3或12，则玩家输庄家胜。若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜；若掷出的点数和为7则庄家胜。含筹码！
'''


def craps_dubo():
	chou_ma = int(input('请输入您手里有多少筹码：'))
	while chou_ma > 0:
		debt = int(input('请输入您要下注的筹码：'))
		if debt > chou_ma:
			print('您的筹码不够，请重新下注！')
			continue
		sum = random.randint(1, 6) + random.randint(1, 6)
		if sum == 7 or sum == 11:
			chou_ma += debt
			print('该局玩家胜出，玩家现有筹码总数%d' % chou_ma)
		elif sum == 2 or sum == 3 or sum == 12:
			chou_ma -= debt
			print('该局庄家胜出，玩家现有筹码总数%d' % chou_ma)
		else:
			while True:
				sum1 = random.randint(1, 6) + random.randint(1, 6)
				if sum1 == sum:
					chou_ma += debt
					print('该局玩家胜出，玩家现有筹码总数%d' % chou_ma)
					break
				elif sum1 == 7:
					chou_ma -= debt
					print('该局庄家胜出，玩家现有筹码总数%d' % chou_ma)
					break


if __name__ == '__main__':
	# shui_xian_hua()
	# wan_mei_shu()
	# bai_qian_bai_ji()
	# fibonacci_sequence()
	craps_dubo()
