#!/usr/bin/python

# lets make the client code
import socket, cv2, pickle, struct, imutils


class SockServer:
    def __init__(self, port):
        self.server_socket          = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host_name              = socket.gethostname()
        self.host_ip                = socket.gethostbyname(self.host_name)
        self.socket_address         = (self.host_ip, port)
        self.port                   = port            
        
    def serverCore(self):
        print('HOST IP: ', self.host_ip)
        
        # Socket Bind
        self.server_socket.bind(self.socket_address) 
        
        # Socket Listen
        self.server_socket.listen(5)
        print("LISTENING AT:", self.socket_address)
        
        
        # Socket Accept
        while True:
            self.client_socket,addr      = self.server_socket.accept()
        
            print('GOT CONNECTION FROM: ', addr)
        
            if self.client_socket:
                vid                 = cv2.VideoCapture(0)
                
                while(vid.isOpened()):
                    img,frame       = vid.read()
                    frame           = imutils.resize(frame,width=320)
                    a               = pickle.dumps(frame)
                    message         = struct.pack("Q",len(a))+a
        
                    self.client_socket.sendall(message)
                    
                    
           


class SockCLient:
    def __init__(self, ip, port):
        # create socket
        self.client_socket       = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host_ip             = ip
        self.port                = port

        self.client_socket.connect((self.host_ip, self.port)) # a tuple

        self.data                = b""
        self.payload_size        = struct.calcsize("Q")
        self.frame               = None
        

    def clientResponse(self):
            
        while len(self.data) < self.payload_size:
            packet      = self.client_socket.recv(4*1024) # 4K
    
            if not packet: break
    
            self.data       += packet
    
        packed_msg_size = self.data[:self.payload_size]
        self.data       = self.data[self.payload_size:]
        msg_size        = struct.unpack("Q",packed_msg_size)[0]
        
        while len(self.data) < msg_size:
            self.data  += self.client_socket.recv(4*1024)
    
        frame_data      = self.data[:msg_size]
        self.data       = self.data[msg_size:]
        frame           = pickle.loads(frame_data)
    
        self.frame = frame
        
