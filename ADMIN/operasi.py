from . import database
import os,time


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
    data["tanggal_booking"] = tgl_booking
    data["nama"] = nama + database.TEMPLATE_DATA_PEMESAN["nama"][len(nama):]
    data["nomor"] = no_telp + database.TEMPLATE_DATA_PEMESAN["nomor"][len(no_telp):]
    data["email"] = email + database.TEMPLATE_DATA_PEMESAN["email"][len(email):]
    data["tagihan"] = tagihan
    data["maskapai"] = maskapai 

    data_str = f'{data["pk"]},{data["tanggal_booking"]}, {data["nama"]},{data["nomor"]},{data["email"]},{maskapai},{data["tagihan"]}'
   
    panjang_data = len(data_str)
   
    try:
        with open(database.DB_PEMESAN,"r+",encoding="utf-8") as file:
            data = file.readlines()
            index = 0
            while True:
                content = data[index]
                data_split = content.split(",")
                cpk = data_split[0]
                if cpk == pk:
                    break

                index += 1

            file.seek(panjang_data*index)
            file.write(data_str)
    except:
        print("Error Dalam Update Data")


def update_penumpang(pk, title, nama, waktu, tanggal, maskapai, jurusan):

    data = database.TEMPLATE_DATA_PENUMPANG.copy()

    data["pk"] = pk
    data["title"] = title 
    data["nama"] = nama + database.TEMPLATE_DATA_PENUMPANG["nama"][len(nama):] 
    data["waktu"] = waktu 
    data["tanggal"] = tanggal + database.TEMPLATE_DATA_PENUMPANG["tanggal"][len(tanggal):]
    data["maskapai"] = maskapai + database.TEMPLATE_DATA_PENUMPANG["maskapai"][len(maskapai):]
    data["jurusan"] = jurusan 

    data_str = f'{data["pk"]}, {data["title"]}, {data["nama"]}, {data["waktu"]}, {data["tanggal"]}, {data["maskapai"]}, {data["jurusan"]}\n'

    panjang_data = len(data_str)

    try:
        with open(database.DB_PENUMPANG,"r+",encoding="utf-8") as file:
            data = file.readlines()
            index = 0
            while True:
                content = data[index]
                data_split = content.split(",")
                cpk = data_split[0]
                if cpk == pk:
                    break

                index += 1

            file.seek(panjang_data*index)
            file.write(data_str)
    except:
        print("Error Dalam Update Data")


def delete_pemesan(pk):
    try:
        with open(database.DB_PEMESAN,"r+",encoding="utf-8") as file:
            data = file.readlines()
            index = 0
            while True:
                content = data[index]
                data_split = content.split(",")
                cpk = data_split[0]
                if cpk == pk:
                    break

                index += 1

            del data[index]
    except:
        print("Error Dalam Update Data")


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