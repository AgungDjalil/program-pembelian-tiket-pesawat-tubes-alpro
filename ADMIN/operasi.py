from . import database


def read(pilihan):
    try:
        with open(f"/home/agung/Documents/alpro/program tiket pesawat /{pilihan}.txt", 'r') as file:
            content = file.readlines()
            return content
    except:
        print("Membaca database error")


def search_data_pemesan(**kwargs):
    try:
        with open(database.DB_PEMESAN, 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_data = kwargs["index"]-1
                if index_data < 0 or index_data > jumlah_buku:
                    return False
                else:   
                    return content[index_data]
            else:
                return content
    except:
        print("Membaca database error")
        return False


def satu_pemesan(pk, tanggal, nama, nomor, email, maskapai, tagihan):
    while(True):
        print("="*90)
        print("Silahkan Pilih Data Apa Yang Ingin Anda Ubah")
        print(f"1. Nama     : {nama}\n2. Nomor    : {nomor}\n3. Email    : {email}\n4. Maskapai : {maskapai}") 

        user_option = input("Pilih Data [1,2,3,4]")
        print("="*90)
        if user_option == "1":
            name = input("Nama : ")
            return name
        elif user_option == "2":
            nomer = input("Nomor : ")
            return nomer
        elif user_option == "3":
            emel = input("Email : ")
            return emel
        elif user_option == "4":
            maskpai = input("Maskapai : ")
            return maskpai
        else:
            print("Nomor Tidak Valid")

        print(f"Data Baru Anda")
        print(f"Nama\t: {name}\nNomor\t: {nomer}\nEmail\t: {emel}\nMaskapai\t: {maskpai}")
       
        sudah = input("Apakah Data Sudah selesai(y/n)?")
        if sudah == "y" or sudah == "Y":
            break

        update(pk, tanggal, name, nomer, emel, maskpai, tagihan)
    


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