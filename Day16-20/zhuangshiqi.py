from functools import wraps
from threading import Lock
from time import time


def record_time(func):
	'''自定义装饰函数的装饰器'''

	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time()
		result = func(*args, **kwargs)
		print(f'{func.__name__}:{time() - start}秒')
		return result

	return wrapper


def record(output):
	'''自定义带参数的装饰器'''

	def decorate(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			start = time()
			result = func(*args, *kwargs)
			output(func.__name__, time() - start)
			return result

		return wrapper

	return decorate


class Record():
	'''自定义装饰器类(通过__call__魔术方法使得对象可以当成函数调用)'''

	def __init__(self, output):
		self.output = output

	def __call__(self, func):
		@wraps(func)
		def warpper(*args, **kwargs):
			start = time()
			result = func(*args, **kwargs)
			self.output(func.__name__, time() - start)
			return result

		return warpper


@record_time
def record_func():
	pass


# 线程不安全
def singleton(cls):
	'''装饰类的装饰器'''
	instances = {}

	@wraps(cls)
	def wrapper(*args, **kwargs):
		if cls not in instances:
			instances[cls] = cls(*args, **kwargs)
		return instances[cls]

	return wrapper


# 线程安全
def singleton(cls):
	instances = {}
	locker = Lock()

	@wraps(cls)
	def wrapper(*args, **kwargs):
		if cls not in instances:
			with locker:
				if cls not in instances:
					instances[cls] = cls(*args, **kwargs)
		return instances[cls]

	return wrapper


@singleton
class President():
	pass


if __name__ == '__main__':
	record_func()
