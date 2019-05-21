'''简单选择排序'''


def select_sort(origin_items, comp=lambda x, y: x < y):
	items = origin_items[:]
	for i in range(len(items) - 1):
		min_index = i
		for j in range(i + 1, len(items)):
			if comp(items[j], items[min_index]):
				min_index = j
		items[i], items[min_index] = items[min_index], items[i]
	return items


'''高质量冒泡排序(搅拌排序)'''


def bubble_sort(origin_items, comp=lambda x, y: x > y):
	items = origin_items[:]
	for i in range(len(items) - 1):
		swapped = False
		for j in range(i, len(items) - 1):
			if comp(items[j], items[j + 1]):
				items[j], items[j + 1] = items[j + 1], items[j]
				swapped = True
			if swapped:
				swapped = False
				for j in range(len(items) - 2 - i, i, -1):
					if comp(items[j - 1], items[j]):
						items[j], items[j - 1] = items[j - 1], items[j]
						swapped = True
			if not swapped:
				break
	return items


'''归并排序(分治法)'''


def merge_sort(items, comp=lambda x, y: x <= y):
	if len(items) < 2:
		return items[:]
	mid = len(items) // 2
	left = merge_sort(items[:mid], comp)
	right = merge_sort(items[mid:], comp)
	return merge(left, right, comp)


def merge(items1, items2, comp):
	'''合并(将两个有序的列表合并成一个有序的列表)'''
	items = []
	index1, index2 = 0, 0
	while index1 < len(items1) and index2 < len(items2):
		if comp(items1[index1], items2[index2]):
			items.append(items1[index1])
			index1 += 1
		else:
			items.append(items2[index2])
			index2 += 1
	items += items1[index1:]
	items += items2[index2:]
	return items


'''顺序查找'''


def seq_search(items, key):
	for index, item in enumerate(items):
		if item == key:
			return index
	return -1


'''折半查找'''


def bin_search(items, key):
	start, end = 0, len(items) - 1
	while start <= end:
		mid = (start + end) // 2
		if key > items[mid]:
			start = mid + 1
		elif key < items[mid]:
			end = mid - 1
		else:
			return mid
	return -1
