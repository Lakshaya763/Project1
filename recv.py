import socket
import time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
my_ip='127.0.0.1'
#--52.2.116.225--jecrc.delvex.io
my_port=9999
my_address=(my_ip,my_port)
#lets create a connection string
s.bind(my_address)
while 4>2:
    data=s.recvfrom(100)
    new_data=data[0]
    final_msg=new_data.decode('ascii')
    print(final_msg)
    #implement file handing print
    time.sleep(2)