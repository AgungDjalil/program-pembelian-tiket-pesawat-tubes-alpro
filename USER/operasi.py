from . import database
from .util import random_string
from time import time
import time, os
from . import inputan


def read(kota):

    try:
        with open(f'/home/agung/Documents/tugas kuliah/alpro/program tiket pesawat /jadwal/{kota}.csv', 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            return content
    except:
        print("Membaca database error")
        return False


def read_plane(**kwargs):

    try:
        with open(f'/home/agung/Documents/tugas kuliah/alpro/program tiket pesawat /jadwal/{kota}.csv', 'r') as file:
            content = file.readlines()
            jumlah_data = len(content)
            if "no_pesawat" in kwargs:
                index_data = kwargs["no_pesawat"]-1
                if index_data < 0 or index_data > jumlah_data:
                    return False
                else:    
                    return content[index_data]
            else:
                return content
    except:
        print("Membaca database error")
        return False


def database_pemesan(maskapai, pemesan, tagihan):

    data_break = pemesan.split(",")
    nama = data_break[0]
    nomor = data_break[1]
    email = data_break[2]
    

    data = database.TEMPLATE_DATA_PEMESAN.copy()

    data["pk"] = random_string(10)
    data["tanggal_booking"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["nama"] = nama + database.TEMPLATE_DATA_PEMESAN["nama"][len(nama):]
    data["nomor"] = nomor + database.TEMPLATE_DATA_PEMESAN["nomor"][len(nomor):]
    data["email"] = email + database.TEMPLATE_DATA_PEMESAN["email"][len(email):]
    data["tagihan"] = "Rp." + str(tagihan)
    data["maskapai"] = maskapai 

    data_str = f'{data["pk"]}, {data["tanggal_booking"]}, {data["nama"]}, {data["nomor"]}, {data["email"]}, {maskapai}, {data["tagihan"]}\n'
    
    try:
        with open(database.DB_PEMESAN,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit ditambahkan boooos, gagal maning")


def database_penumpang(title, nama, thn_tgl_bln, waktu, maskapai, jurusan):
    thn_tgl_bln = str(thn_tgl_bln)
    data = database.TEMPLATE_DATA_PENUMPANG.copy()
    data["pk"] = random_string(10)
    data["title"] = title 
    data["nama"] = nama + database.TEMPLATE_DATA_PENUMPANG["nama"][len(nama):] 
    data["waktu"] = waktu 
    data["tanggal"] = thn_tgl_bln + database.TEMPLATE_DATA_PENUMPANG["tanggal"][len(thn_tgl_bln):]
    data["maskapai"] = maskapai + database.TEMPLATE_DATA_PENUMPANG["maskapai"][len(maskapai):]
    data["jurusan"] = jurusan 

    data_str = f'{data["pk"]}, {data["title"]}, {data["nama"]}, {data["waktu"]}, {data["tanggal"]}, {data["maskapai"]}, {data["jurusan"]}\n'

    try:
        with open(database.DB_PENUMPANG,"a",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data tidak dapat ditambahkan")


def data_penumpang(total_penumpang, thn_tgl_bln, waktu, maskapai, Jurusan):
    n = 1
    penumpang = []
    while n <= total_penumpang:
        print("Passenger Details")
        titel = inputan.title()
        nama_depan = inputan.nama_depan()
        nama_belakang = inputan.nama_belakang()
        nama = " ".join({nama_depan, nama_belakang})

        data = titel + nama

        penumpang.append(data)
        database_penumpang(titel, nama, thn_tgl_bln, waktu, maskapai, Jurusan)
        n += 1

    return penumpang


def untuk_dewasa(dewasa, harga):
    if dewasa == 0:
        harga_dewasa = 0
        return harga_dewasa
    elif dewasa <= 6:
        harga_dewasa = dewasa * harga
        return harga_dewasa


def untuk_anak(anak, harga):
    if anak <= 3:
        diskon_anak = (harga * anak * 5) / 100
        harga_anak = (harga * anak) - diskon_anak
        return harga_anak
    else:
        harga_anak = 0
        return harga_anak


def untuk_bayi(bayi, harga):
    if bayi == 0:
        harga_bayi = 0
        return harga_bayi
    else:
        diskon_bayi = (bayi * harga * 15) / 100
        harga_bayi = (bayi * harga) - diskon_bayi
        return harga_bayi


def loading():
    os_name = os.name
    if os_name == "posix":
        os.system("clear")
        print("loading....")
        time.sleep(0)
        os.system("clear")
        
    else:
        os.system("cls")
        print("Loading....")
        time.sleep(4)
        os.system("cls")