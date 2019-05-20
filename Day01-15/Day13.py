import tkinter
import tkinter.messagebox
from multiprocessing import Process, Queue
from threading import Thread
from time import time


# 例子1：将耗时间的任务放到线程中以获得更好的用户体验。
def test1_main():
	class DownloadTaskHandler(Thread):
		def run(self):
			time.sleep(10)
			tkinter.messagebox.showinfo('提示', '下载完成!')
			# 启用下载按钮
			button1.config(state=tkinter.NORMAL)

	def download():
		# 禁用下载按钮
		button1.config(state=tkinter.DISABLED)
		# 通过daemon参数将线程设置为守护进程(主程序退出后就不再保留执行)
		# 在线程中处理耗时间的下载任务
		DownloadTaskHandler(daemon=True).start()

	def show_about():
		tkinter.messagebox.showinfo('关于', '作者：Allen')

	top = tkinter.Tk()
	top.title('单线程')
	top.geometry('200x150')
	top.wm_attributes('-topmost', 1)

	panel = tkinter.Frame(top)
	button1 = tkinter.Button(panel, text='下载', command=download)
	button1.pack(side='left')
	button2 = tkinter.Button(panel, text='关于', command=show_about)
	button2.pack(side='right')
	panel.pack(side='bottom')

	tkinter.mainloop()


# 例子2：使用多进程对复杂任务进行“分而治之”

def task_handler(curr_list, result_queue):
	total = 0
	for number in curr_list:
		total += number
	result_queue.put(total)


def test2_main():
	processes = []
	number_list = [x for x in range(1, 100000001)]
	result_queue = Queue()
	index = 0
	# 启动8个进程将数据切片后进行运算
	for _ in range(8):
		p = Process(target=task_handler, args=(number_list[index:index + 12500000], result_queue))
		index += 12500000
		processes.append(p)
		p.start()
	# 开始记录所有进程执行完成花费的时间
	start = time()
	for p in processes:
		p.join()
	# 合并执行结果
	total = 0
	while not result_queue.empty():
		total += result_queue.get()
	print(total)
	end = time()
	print('Execution time:', (end - start), 's', sep='')


if __name__ == '__main__':
	test2_main()
