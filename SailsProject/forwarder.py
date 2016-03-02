from multiprocessing import Process
import socket
import json

HOST = ""
BUF_SIZE = 1024
CONFIG_FILE_PATH = './.tmp/localDiskDb.db';
CONFIG_DATA  = {}
BACKLOG = 5


def forwarder(sourcePort,arrayOfDestination):
    #create socket and listen
    forwarder = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    forwarder.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    forwarder.bind(('', sourcePort))
    forwarder.listen(BACKLOG)
    length = len(arrayOfDestination)
    count = 0
    while True:
        client_socket, address = forwarder.accept()
        destination = arrayOfDestination[count%length]
        print(destination["dest_port"])
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((destination["dest_ip"], destination["dest_port"]))
        print 'Connection Established With Source:', address
        print 'Connection Established With Destination: IP',destination["dest_ip"],', Port', destination["dest_port"]
        process = Process(target=forward, args=(client_socket, server_socket))
        process.start()
        process2 = Process(target=forward, args=(server_socket, client_socket))
        process2.start()
        count = count + 1



def forward(client, server):
	while True:
		try:
			data = client.recv(BUF_SIZE)
			if data:
				server.sendall(data)
			else:
				client.close()
				server.shutdown(socket.SHUT_WR)
				return
		except:
			server.shutdown(socket.SHUT_WR)
			client.close()
			return

def read_data():
    with open(CONFIG_FILE_PATH) as data_file:
		data = json.load(data_file)
    ports = data["data"]["ports"]
    for num in range(0,len(ports)):
        data = ports[num]
        src_port = data["source_port"]
        if src_port not in CONFIG_DATA:
            CONFIG_DATA[src_port]=[]
        CONFIG_DATA[src_port].append({"dest_port":data["dest_port"], "dest_ip":data["dest_ip"]})

def main():
    read_data()
    for sourcePort, arrayOfDestination in CONFIG_DATA.iteritems():
		process = Process(target=forwarder, args=(sourcePort,arrayOfDestination,))
		process.start()
    while True:
        pass


if __name__ == '__main__':
	main()
