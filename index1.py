# kegiatan 1
print "<!DOCTYPE html>"
print
print """<html>
<head>
<title> kegiatan 1</title>
</head>
<body>"""
print """<table>
<tr>
    <th rowspan='7' width='140' >FOTO</th>
    <td><h3>Data Diri</h3></td>
</tr>
<tr>
    <td>NAMA : Nimas Woro Pangesti</td>
</tr>
<tr>
    <td>ALAMAT : Sidorejo, Borangan, Manisrenggo, Klaten</td>
</tr>
<tr>
    <td>TEMPAT, TANGGAL LAHIR : Klaten, 14 April 2000</td>
</tr>
<tr>
    <td>TEMPAT WISATA FAVORIT : ALAM</td>
</tr>
<tr>
    <td>MOTTO : You Can Do It</td>
</tr>
</table>"""
print "</body></html>"

# kegiatan 2
print "<!DOCTYPE html>"
print
print """<html>
<head>
<title> kegiatan 2</title>
</head>
<body>"""
print """<table>
<tr>
    <th rowspan='6' width='120' >FOTO</th>
    <td><h3>Data Diri</h3></td>
</tr>
<tr>
    <td>NAMA : Nimas Woro Pangesti</td>
</tr>
<tr>
    <td>ALAMAT : Sidorejo, Borangan, Manisrenggo, Klaten</td>
</tr>
<tr>
    <td>TEMPAT, TANGGAL LAHIR : Klaten, 14 April 2000</td>
</tr>
<tr>
    <td>TEMPAT WISATA FAVORIT : ALAM</td>
</tr>
<tr>
    <td>MOTTO : You Can Do It</td>
</tr>
</table>"""
print "</body></html>"

#kegiatan 3
def hitung (panjang, lebar, tinggi):
    p=panjang
    l=lebar
    t=tinggi
    luas=2*(p*l+p*t+l*t)
    return luas
panjang=3
lebar=4
tinggi=5
print"<!DOCTYPE html>"
print
print"""<html>
<head><title>Luas Bangun</title></head>
<body>"""
print"""<table>
<tr>
   <th rowspan='8' weight='150'>GAMBAR</th>
   <td><h3>Bangun Geometri<h3></td>
</tr>
<tr>
    <td>Nama Bangun</td>
    <td>:</td>
    <td>Balok</td>
</tr>
<tr>
    <td>Dimensi(2D/3D)</td>
    <td>:</td>
    <td>3D</td>
</tr>
<tr>
    <td>Rumus Luas</td>
    <td>:</td>
    <td>2*(p*l+p*t+l*t)</td>
</tr>
<tr>
    <td>Panjang</td>
    <td>:</td>
    <td>3</td>
</tr>
""".format(panjang)
print"""<tr>
    <td>Lebar</td>
    <td>:</td>
    <td>4</td>
</tr>
""".format(lebar)
print"""<tr>
    <td>Tinggi</td>
    <td>:</td>
    <td>5</td>
</tr>
""".format(tinggi)
print"""<tr>
    <td>Luas</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(hitung(panjang,lebar,tinggi))
print """
</table>"""
print"</body></html>"

