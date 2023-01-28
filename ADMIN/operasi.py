from . import database
import os
import time


def read(pilihan):
    try:
        with open(f"/home/agung/Documents/tugas kuliah/alpro/program tiket pesawat /{pilihan}.txt", 'r') as file:
            content = file.readlines()
            return content
    except:
        print("Membaca database error")


def search(no_pk, pilihan):
    try:
        with open(f"/home/agung/Documents/tugas kuliah/alpro/program tiket pesawat /{pilihan}.txt", 'r') as file:
            content = file.readlines()
            jmlh_data = len(content)
            for index in range(jmlh_data):
                data = content[index]
                data_split = data.split(",")
                pk = data_split[0]
                if pk == no_pk:
                    return data_split
                    break
    except:
        print("Membaca database error")
        return False


def update_pemesan(pk, tgl_booking, nama, no_telp, email, maskapai, tagihan):

    data = database.TEMPLATE_DATA_PEMESAN.copy()

    data["pk"] = pk
    data["tanggal_booking"] = str(tgl_booking)
    data["nama"] = nama + database.TEMPLATE_DATA_PEMESAN["nama"][len(nama):]
    data["nomor"] = no_telp + \
        database.TEMPLATE_DATA_PEMESAN["nomor"][len(no_telp):]
    data["email"] = email + \
        database.TEMPLATE_DATA_PEMESAN["email"][len(email):]
    data["tagihan"] = tagihan + \
        database.TEMPLATE_DATA_PEMESAN["tagihan"][len(tagihan):]
    data["maskapai"] = maskapai + \
        database.TEMPLATE_DATA_PEMESAN["maskapai"][len(maskapai):]

    data_str = f'{data["pk"]},{data["tanggal_booking"]},{data["nama"]},{data["nomor"]},{data["email"]},{data["maskapai"]},{data["tagihan"]}'

    panjang_data = len(data_str)

    try:
        with open(database.DB_PEMESAN, "r+", encoding="utf-8") as file:
            data = file.readlines()
            index = cari_index(pk, data)

            file.seek(panjang_data*index)
            file.write(data_str)

    except:
        print("Error Dalam Update Data")


def update_penumpang(pk, title, nama, waktu, tanggal, maskapai, jurusan):

    data = database.TEMPLATE_DATA_PENUMPANG.copy()

    data["pk"] = pk
    data["title"] = title
    data["nama"] = nama + database.TEMPLATE_DATA_PENUMPANG["nama"][len(nama):]
    data["waktu"] = waktu + \
        database.TEMPLATE_DATA_PENUMPANG["waktu"][len(waktu):]
    data["tanggal"] = tanggal + \
        database.TEMPLATE_DATA_PENUMPANG["tanggal"][len(tanggal):]
    data["maskapai"] = maskapai + \
        database.TEMPLATE_DATA_PENUMPANG["maskapai"][len(maskapai):]
    data["jurusan"] = jurusan + \
        database.TEMPLATE_DATA_PENUMPANG["jurusan"][len(jurusan):]

    data_str = f'{data["pk"]},{data["title"]},{data["nama"]},{data["waktu"]},{data["tanggal"]},{data["maskapai"]},{data["jurusan"]}'

    panjang_data = len(data_str)

    try:
        with open(database.DB_PENUMPANG, "r+", encoding="utf-8") as file:
            data = file.readlines()
            index = cari_index(pk, data)

            file.seek(panjang_data*index)
            file.write(data_str)
    except:
        print("Error Dalam Update Data")


def data_sort(**pilihan):
    try:
        with open(f"/home/agung/Documents/tugas kuliah/alpro/program tiket pesawat /{pilihan['nama_file']}.txt", "r+", encoding="utf-8") as file:
            data = file.readlines()
            data_tuple = [tuple(line.strip().split(',')) for line in data]
            sorting = sorted(data_tuple, key=lambda content:content[2])
            return sorting
    except:
        return False


def delete_pemesan(pk):
    try:
        with open(database.DB_PEMESAN, "r") as file:
            content = file.readlines()
            data_ke = cari_index(pk, content)

            with open(database.DB_PEMESAN, "w") as file:
                for index, data in enumerate(content):
                    if index != data_ke:
                        file.write(data)
    except:
        print("Error Dalam Delete Data")


def delete_penumpang(pk):
    try:
        with open(database.DB_PENUMPANG, "r") as file:
            content = file.readlines()
            data_ke = cari_index(pk, content)

            with open(database.DB_PENUMPANG, "w") as file:
                for index, data in enumerate(content):
                    if index != data_ke:
                        file.write(data)
    except:
        print("Error Dalam Delete Data")


def cari_index(pk, data):
    counter = 0
    while True:
        content = data[counter]
        data_split = content.split(",")
        cpk = data_split[0]
        if cpk == pk:
            return counter
            break

        counter += 1


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
        time.sleep(2)
        os.system("cls")
