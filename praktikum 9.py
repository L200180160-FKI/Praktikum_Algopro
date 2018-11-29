# kegiatan 1
berkas = open("L200180160.txt", "w")
berkas.write("L200180160.\n")
berkas.write("14-04-2000.\n")
berkas.write("Nimas Woro Pangesti.\n")
berkas.close()

#kegiatan 2
berkas = open("L200180160.txt", "w")
berkas.write("Nimas Woro Pangesti.\n")
berkas.write("L200180160.\n")
berkas.write("Klaten.\n")
berkas.write("14-04-2000.\n")
berkas.close()

import shelve
x = open ("L200180160.txt", "r")
Nama = x.readline()
Nim = x.readline()
kotalahir = x.readline()
TL = x.readline()
x.close()

x = shelve.open("Nimas")
x['a'] = [Nama, Nim, kotalahir, TL]
x.close()

x = shelve.open("Nimas")

print x['a'][0]
print x['a'][1]
print x['a'][2]
print x['a'][3]

#kegiatan 3
import shelve
x = open("L200180160.txt","r")
Nama = x.readline()
Nim = x.readline()
kotalahir = x.readline()
TL = x.readline()
x.close()

x = shelve.open("Nimas")
x['b'] = [Nama, Nim, kotalahir, TL]
x.close()

#kegiatan 4
import shelve
x = shelve.open("Nimas")
print 'Nama :' , x['b'][0]
print 'Nim :' , x['b'][1]
print 'kotalahir :',  x['b'][2]
print 'TL :' , x['b'][3]


