import threading

from sender import Sender
from tcpserver import TCPServer


class Stream:
    def __init__(self):
        self.sender = None

        self._server_in_buf = []

        def callback(address, queue, data):
            queue.put(bytes('ACK', 'utf8'))
            self._server_in_buf.append(data)

        self.tcp_server = TCPServer(read_callback=callback)
        server_thread = threading.Thread(target=self.tcp_server.run)
        server_thread.start()

        self.ip = Sender.parse_ip(self.tcp_server.ip)
        self.port = Sender.parse_port(self.tcp_server.port)

    def get_server_address(self):
        return self.ip, self.port

    def clear_in_buff(self):
        self._server_in_buf = []

    def add_sender(self, server_address, delay):
        self.sender = Sender(server_address=server_address, delay=delay)
        

    def add_message_to_out_buff(self, message):
        self.sender.add_message_to_out_buff(message)

    def read_in_buf(self):
        ret = self._server_in_buf
        self.clear_in_buff()
        return ret
        
    def send_messages(self):
        try:
            self.sender.send_message()
        except IOError as e:
            print('stream: error in sending message', e)
