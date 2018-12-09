# kegiatan 1
# nama berkas: p_tcpser.py
# TCP server untuk client p_tcpcli.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s. bind(("", 50002))
s.listen(5)
print"server penjawab otomatis sudah siap"
data = ''
kamus = {'nama' : 'nimas woro pangesti',
         'nim' : 'L200180160',
         'angkatan' : '2018'}
        
while data.lower() != 'keluar' :
    komm, addr = s.accept()
    while data.lower() != 'keluar':
        data = komm.recv(1024)
        if data.lower() == 'keluar' :
            s.close()
            break
        print 'pertanyaa:', data
        if kamus.has_key(data) :
            komm.send(kamus[data])
        else:
            komm.send('maaf, perintah tidak dimengerti')


#kegiatan 2
#nama berkas: p_ycpser.py
#TCP Server untuk client p_tcpc.py

import socket
import platform
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50003))
s.listen(5)
print "Server penjawab otomatis sudah siap"
data = ''
kamus = {'machine' : platform.machine() ,
         'release' : platform.release() ,
         'system' : platform.system() ,
         'version' : platform.version() ,
         'node' : platform.node()}
while data.lower() != 'quit' :
    komm, addr = s.accept()
    while data.lower() != 'quit':
        data = komm.recv(1024)
        if data.lower() == 'quit' :
            s.close()
            break
        print 'command:', data
        if kamus.has_key(data) :
            komm.send(kamus[data])
        else:
            komm.send('unknown command')


#kegiatan 3
#nama berkas: p_ucpser.py
#TCP server untuk client p_tcpcl.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s. bind(("", 50002))
s.listen(5)
print"server penjawab otomatis sudah siap"
data = ''
        
while data.lower() != 'q' :
    komm, addr = s.accept()
    while data.lower() != 'q':
        data = komm.recv(1024)
        if data.lower() == 'keluar' :
            s.close()
            break
        print ('pesan:', data)
        komm.send('parameter dicatat')
        t=komm.send(1024)
        if t=='hitung':
            masuk=int(data)
            p=2*( p*l + p*t + l*t )
            p=int(h)
            masuk=str(data)
            komm.send('luas permukaan balok'+data+'adalah'+p)
s.close()
            
                                   
