Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> ##PRAKTIKUM 6 KEGIATAN 1 
>>> namalengkap
'Nimas Woro Pangesti'
>>> namapanggilan
'Nimas'
>>> nim
'L200180160'
>>> prodi
'Informatika'
>>> alamat
'Sidorejo, Borangan, Manisrenggo, Klaten'
>>> tempatlahir
'Klaten'
>>> tanggallahir
'14 April 2000'
>>> namaayah
'Wahyudi Martono'
>>> namaibu
'Prih Hastuti'
>>> hobi
'menyanyi'
>>> umur
'18'
>>> ##PRAKTIKUM 6 KEGIATAN 2
>>> nama
'Nimas Woro Pangesti'
>>> tanggallahir
'14 April 2000'
>>> nim
'L200180160'
>>> namaSingkat
'N.W.Pangesti'
>>> username
'N142000'
>>> password
'Nim160'
>>> ##PRAKTIKUM 6 KEGIATAN 3
>>> Nama = 'Nimas Woro Pangesti'
>>> NIM = 'L200180160'
>>> X = '1' + NIM[7:] # Didalam string, digunakan angka 1 dengan slicing yang dimulai dari angka/huruf ke tujuh dari variabel NIM sampai selesai
>>> print (X) # menampilkan variabel X
1160
>>> a = int (X) # menampilkan string ke integer
>>> print (a) # menampilkan variabel a
1160
>>> b = len(Nama) # konversi string dalam veriabel Nama ke dalam angka
>>> print (b) # menampilkan variabel b
19
>>> type (a) # menampilkan type data dari variabel a
<type 'int'>
>>> type (b) # menampilkan type data dari variabel b
<type 'int'>
>>> a / b # operasi pembagian antara bilangan dari variabel a dengan b. type data yang bisa untuk membagi bilangan hanya bila data tersebut bertype integer/float
61
>>> a // b # operasi pembagian antar bilangan dengan pembulatan ke bawah. type data yang bisa untuk membagi bilangan hanya bila data bertype integer/float
61
>>> 10 * (a-999) # operasi perkalian ini dapat digunakan untuk mengalikan data dengan type integer maupun float
1610
>>> b ** 2 # operasi ini digunakan digunakan untuk perpangkatan, type data yang dapat digunakan dalam operasi ini diantaranya integer dan float
361
>>> a % b # operasi ini digunakan untuk memunculkan sisa hasil bagi
1
>>> c = 12.5 #variabel c berupa angka yang terdapat koma berarti type data pada variabel c yaitu float
>>> type (c) # menmpilkan type data dari variabel c
<type 'float'>
>>> a / c # operasi pembagian antara bilangan dari variabel a dengan c. type data yang bisa untuk membagi bilangan hanya bila data tersebut bertype integer/float
92.8
>>> a // c # operasi pembagian antar bilangan dengan pembulatan ke bawah. type data yang bisa untuk membagi bilangan hanya bila data bertype integer/float
92.0
>>> a % c # operasi ini digunakan untuk memunculkan sisa hasil bagi
10.0
>>> c > b # operasi ini digunakan untuk menampilkan perbandingan lebih dari. type data ini adalah boolean
False
>>> type (c > b) # menampilkan type data dari (c > b)
<type 'bool'>
>>> a > b and b > c # pada data terdapat dua pernyataan 1160 > 19 dan 19 > 12.5. karena kedua pernyataan tersebut dihubungkan dengan operator logika "and" maka akan menghasilkan dua kemungkinan nilai, yaitu true atau false
True
>>> a > 1100 or b < 10 # operator logika yang digunakan pada data adalah "or" apabila salah satu dari pernyataan benar akan menghasilkan nilai benar . Dari pernyataan disamping diartikan 1160 > 1100 atau 19 < 10 . Dengan 1160 > 1100 maka pernyataan ini benar sedangakan pernyataan ini 19 < 10 salah maka nilai yang akan di dapat adalah benar
True
.
>>> ##PRAKTIKUM 6 KEGIATAN 4 
>>> Nama = 'Nimas Woro Pangesti'
>>> NIM = 160
>>> Tinggi = 1.56
>>> Berat = 58
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama) # Sebuah Tuple
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama] # Sebuah List
>>> type (Aku) # menampilkan type data dari variabel aku
<type 'tuple'>
>>> Aku [0] # menampilkan elemen tuple indeks 0
2000
>>> a = NIM % 4 ; Aku[a] # NIM 160 dibagi 4 sisa hasil bagi adalah 0. Lalu indeks 0 dimasukkan kedalam variabel Aku
2000
>>> type (Aku[a]) # menampilkan type data dari elemen tuple indeks a
<type 'int'>
>>> Aku [a:4] # slicing dimulai indeks ke 0 sampai indeks 4
(2000, 58, 1.56, 160)
>>> type (Aku [4]) # menampilkan type data dari elemen tuple indeks 4
<type 'str'>
>>> Aku [0] = 'ok' # hasilnya ERROR karena elemen sebuah tuple tidak dapat diubah

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    Aku [0] = 'ok' # hasilnya ERROR karena elemen sebuah tuple tidak dapat diubah
TypeError: 'tuple' object does not support item assignment
>>> type (Data) # menampilkan type data dari variabel Data
<type 'list'>
>>> type (Data[4]) # menampilkan type data dari elemen list 4
<type 'str'>
>>> Data [4][5] # menampilkan list indeks 5 pada list 4
' '
>>> Data [4] [a:6] # menampilkan list 0 sampai 5 dari list 4
'Nimas '
>>> Data [0] = 'ok' ; Data #meubah elemen list pada indeks 0 menjadi ok
['ok', 58, 1.56, 160, 'Nimas Woro Pangesti']
>>> Data [-a] # menampilkan huruf/angka terakhir pada indeks ke 0 dari list
'ok'
>>> 


