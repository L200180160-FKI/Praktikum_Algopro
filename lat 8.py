# kegiatan 1. Membuat modul
a = {'Nama' : 'Nimas Woro Pangesti','Panggilan' : 'Nimas','NIM' : 'L200180160',
     'Umur' : '18','Alamat' : 'Klaten','Fakultas' : 'FKI','Prodi' : 'Informatika'}
print "Pilihan yang tersedia:"
print "N menampilakn Nama"
print "M menampilkan Panggilan"
print "I menampilkan NIM"
print "L menampilkan Alamat"
print "F menampilkan Fakultas"
print "P menampilkan Prodi"
print "U menampilkan Umur"

def Nama():
    "menampilkan data diri"
    print 'Nama:' + a['Nama']

def Panggilan():
    "menampilkan data diri"
    print 'Panggilan:' + a['Panggilan']

def NIM():
    "menampilkan data diri"
    print 'NIM:' + a['NIM']

def Umur():
    "menampilkan data diri"
    print 'Umur:' + a['Umur']

def Alamat():
    "menampilkan data diri"
    print 'Alamat:' + a['Alamat']

def Fakultas():
    "menampilkan data diri"
    print 'Fakultas:' + a['Fakultas']

def Prodi():
    "menampilkan data diri"
    print 'Prodi:' + a['Prodi']

repeat = True

while repeat :
    x = raw_input("Pilihan Saudara :")
    if x=="N" :
        Nama()
    elif x=="I" :
        NIM()
    elif x=="M" :
        Panggilan()
    elif x=="L" :
        Alamat()
    elif x=="F" :
        Fakultas()
    elif x=="P" :
        Prodi()
    elif x=="U" :
        Umur()
    elif x=="k" :
        print "TERIMA KASIH."
        repeat = False

# Kegiatan 2. Membuat fungsi
x = int(input('Masukkan Angka Suhu:'))
y = str(input('Jenis Suhu:'))

fah = ['F','f','fahrenheit','Fahrenheit']
cel = ['C','c','celcius','Celcius']

if y in fah:
    ub = str(input('Ingin mengubah ke bentuk celcius?'))
    uby = ['Ya', 'ya']
    if ub in uby:
        d = x - 32
        print('Suhunya adalah', d, 'celcius')
    else:
        print('Suhunya adalah', b, 'fahrenheit')
else:
    ug = str(input('Ingin mengubah ke bentuk fahrenheit?'))
    ugy = ['Ya','ya']
    if ug in ugy:
        g = x -32
        print('Suhunya adalah', g, 'fahrenheit')
    else:
        print('Suhunya adalah', x, 'celcius')





