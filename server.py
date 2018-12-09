#kegiatan 1
# nama berkas: p_tcpcli.py
# Client TCP untuk server p_tcpser.py
import socket

hostname = 'localhost'
pesan = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50002))
while pesan.lower() != 'keluar' :
    pesan = raw_input('perintah :')
    s.send(pesan)
    if pesan.lower() != 'keluar' :
        respons = s.recv(1024)
        print 'jawab:', respons
    else :
        print "siap!!"
s.close()


#kegiatan 2
#nama berkas: p_ycpser.py
#Client TCP untuk server p_tcpc.py

import socket
import platform

hostname = 'localhost'
pesan = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50003))
while pesan.lower() != 'quit' :
    pesan = raw_input('command :')
    s.send(pesan)
    if pesan.lower() != 'quit' :
        respons = s.recv(1024)
        print 'jawab:', respons
    else :
        print "siap!!"
s.close()

#kegiatan 3
# nama berkas: p_ucpser.py
# Client TCP untuk server p_tcpcl.py
import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50002))
print('menghitung luas permukaan balok')
for i in range(0,3):
    keluar=raw_input('pesan:')
    s.send(keluar)
    r=s.recv(1024)
    r=str(r)
    print('respon:',r)
    if keluar=='keluar':
        s.close()
s.close()
s.close()

