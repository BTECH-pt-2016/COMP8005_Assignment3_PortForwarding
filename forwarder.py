from multiprocessing import Process
import socket
import json

HOST = ""
BUF_SIZE = 1024
CONFIG_FILE_PATH = './localDiskDb.db';
CONFIG_DATA  = []
BACKLOG = 5

def server(settings):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('', int(settings["source_port"])));
	print(int(settings["source_port"]));
	server.listen(BACKLOG)
	while True:
		client_socket, address = server.accept()
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_socket.connect((settings["dest_ip"], int(settings["dest_port"])))
		print 'Connection Established With:', address
		process = Process(target=forward, args=(client_socket, server_socket))
		process.start()
		process2 = Process(target=forward, args=(server_socket, client_socket))
		process2.start()

def forward(client, server):
	while True:
		try:
			data = client.recv(BUF_SIZE)
			if data:
				print("sending data to the destination:", data)
				server.sendall(data)
			else:
				print("closing connection with client")
				client.close()
				server.shutdown(socket.SHUT_WR)
				return
		except:
			print("closing connection with client2")
			server.shutdown(socket.SHUT_WR)
			client.close()
			return

def main():
	with open(CONFIG_FILE_PATH) as data_file:
		data = json.load(data_file)
	CONFIG_DATA = data["data"]["ports"]
	for num in range(0,len(CONFIG_DATA)):
		data = CONFIG_DATA[num]
		process = Process(target=server, args=(data,))
		process.start()
	while True:
		pass

if __name__ == '__main__':
	main()
