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
            for data in len(str(content)):
                dataa = content[data]
                datab = dataa.split(",")
                pk = datab[0]
                print(pk)
                if pk == no_pk:
                    print(data)
                    return data
                    break
    except:
        print("Membaca database error")
        return False


def update(pk, tanggal, nama, nomor, email, maskapai, tagihan):
    data = database.TEMPLATE_DATA_PEMESAN.copy()

    data["pk"] = pk
    data["tanggal_booking"] = tanggal
    data["nama"] = nama + database.TEMPLATE_DATA_PEMESAN["nama"][len(nama):]
    data["nomor"] = nomor + database.TEMPLATE_DATA_PEMESAN["nomor"][len(nomor):]
    data["email"] = email + database.TEMPLATE_DATA_PEMESAN["email"][len(email):]
    data["tagihan"] = tagihan
    data["maskapai"] = maskapai 

    data_str = f' {data["pk"]}, {data["tanggal_booking"]}, {data["nama"]}, {data["nomor"]}, {data["email"]}, {maskapai}, {data["tagihan"]}\n'
    
    try:
        with open(database.DB_PEMESAN,'r+',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit ditambahkan boooos, gagal maning")


def loading():
    os_name = os.name
    if os_name == "posix":
        os.system("clear")
        print("loading....")
        time.sleep(2)
        os.system("clear")
        
    else:
        os.system("cls")
        print("Loading....")
        time.sleep(2)
        os.system("cls")