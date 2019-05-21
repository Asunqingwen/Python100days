# 服务器代码：

from base64 import b64encode
from json import dumps, loads
from socket import socket
from threading import Thread


def server_main():
	# 自定义线程类
	class FileTransferHandler(Thread):
		def __init__(self, cclient):
			super(FileTransferHandler, self).__init__()
			self.cclient = cclient

		def run(self):
			my_dict = {}
			my_dict['filename'] = 'guido.jpg'
			# JSON是纯文本不能携带二进制数据
			# 所以图片的二进制数据要处理成base64编码
			my_dict['filedata'] = data
			# 通过dumps函数将字典处理成JSON字符串
			json_str = dumps(my_dict)
			# 发送JSON字符串
			self.cclient.send(json_str.encode('utf-8'))
			self.cclient.close()

	# 1.创建套接字对象并指定使用哪种传输服务
	server = socket()
	# 2.绑定IP地址和端口(区分不同的服务)
	server.bind(('127.0.0.1', 1111))
	# 3.开启监听 - 监听客户端连接到服务器
	server.listen(512)
	print('服务器启动开始监听...')
	with open('guido.jpg', 'rb') as f:
		# 将二进制数据处理成base64再解码成字符串
		data = b64encode(f.read()).decode('utf-8')
	while True:
		client, addr = server.accept()
		# 启动一个线程来处理客户端的请求
		FileTransferHandler(client).start()


# 客户端代码
def client_main():
	client = socket()
	client.connect(('127.0.0.1', 1111))
	# 定义一个保存二进制数据的对象
	in_data = bytes()
	# 由于不知道服务器发送的数据有多大，每次接收1024字节
	data = client.recv(1024)
	while data:
		# 将收到的数据拼接起来
		in_data += data
		data = client.recv(1024)
	# 将收到的二进制数据解码成JSON字符串并转换成词典
	# loads函数的作用就是将JSON字符串转成字典对象
	my_dict = loads(in_data.decode('utf-8'))
	filename = my_dict['filename']
	filedata = my_dict['filedata'].encode('utf-8')
	with open('./' + filename, 'wb') as f:
		# 将base64格式的数据解码成二进制数据并写入文件
		f.write(b64encode(filedata))
	print('图片已保存。')


if __name__ == '__main__':
	pass
