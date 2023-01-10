from . import operasi
import os

### Read Data
def read_console(pilih):
    pilih.lower()
    pilihan = "".join(["data", pilih])
   
    data_file = operasi.read(pilihan)
    
    match pilih:
        case "pemesan"   : pemesan_data(data_file)
        case "penumpang" : penumpang_data(data_file)  

### Search Data
def search_console(pilih):
    operasi.loading()
    pilih.lower()
    pilihan = "".join(["data", pilih])
    print("")

    while(True):
        no_pk = str(input("Masukkan PK\t: "))    
        data = operasi.search(no_pk, pilihan)
        if data:
            break
        else:
            print("No PK Tidak Valid, Masukkan sekali Lagi")

    if pilih == "pemesan":
        operasi.loading()
        nama = data[2]
        no_telp = data[3]
        email = data[4]
        maskapai = data[5]
        tagihan = data[6]
        view_data_pemesan(nama, no_telp, email, maskapai, tagihan)
    elif pilih == "penumpang":
        operasi.loading()
        title = data[1]
        nama = data[2]
        waktu = data[3]
        tanggal = data[4]
        maskapai = data[5]
        tujuan = data[6]
        view_data_penumpang(title, nama, tujuan, waktu, maskapai, tanggal)
       
### Update Data
def update_console(pilih):
    operasi.loading()
    pilih.lower()
    pilihan = "".join(["data", pilih])
    print("")

    while(True):
        no_pk = str(input("Masukkan PK\t: "))    
        data = operasi.search(no_pk, pilihan)
        if data:
            break
        else:
            print("No PK Tidak Valid, Masukkan sekali Lagi")

    match pilih:
        case "pemesan"   : update_pemesan(data)
        case "penumpang" : update_penumpang(data)


def delete_console(pilih):
    operasi.loading()
    pilih.lower()
    pilihan = "".join(["data", pilih])

    while(True):
        no_pk = str(input("Masukkan PK\t: "))    
        data = operasi.search(no_pk, pilihan)
        if data:
            break
        else:
            print("No PK Tidak Valid, Masukkan sekali Lagi")

    nama = data[2]
    no_telp = data[3]
    email = data[4]
    maskapai = data[5]
    tagihan = data[6]
    view_data_pemesan(nama, no_telp, email, maskapai, tagihan)
    pk = data[0]

    usr_option = input("Yakin Ingin Dihapus(y/t)? ".lower())
    if usr_option == "y":
        match pilih:
            case "pemesan"   : operasi.delete_pemesan(pk)
            case "penumpang" : operasi.delete_penumpang(pk)   


def pemesan_data(data_file):
    ## header
    no = "NO"
    tanggal = "TANGGAL"
    nama = "NAMA"
    nomor = "NOMOR TELP"
    email = "EMAIL"
    tagihan = "TAGIHAN"

    print("="*56)
    print(f"{no:3} | {tanggal:15} | {nama:20} | {nomor:10} | {tagihan:.10}")
    print("-"*56)

    ## content
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        tanggal = data_break[1]
        nama = data_break[2]
        nomor = data_break[3]
        email = data_break[2]
        maskapai = data_break[5]
        tagihan = data_break[6]
        print(f"{index+1:3} | {tanggal:.15} | {nama:.20} | {nomor:.10} | {tagihan:.10}\n")

    ## footer
    print("="*56)

      
def penumpang_data(data_file):
    ## Header
    no = "NO"
    nama = "NAMA"
    waktu = "WAKTU"
    tanggal = "TANGGAL"
    maskapai = "MASKAPAI"
 
    print("="*56)
    print(f"{no:2} | {nama:10} | {waktu:10} | {tanggal:10} | {maskapai:10}")
    print("-"*56)
            
    ## Content
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        title = data_break[1]
        nama = data_break[2]
        waktu = data_break[3]
        tanggal = data_break[4]
        maskapai = data_break[5]
        nama = " ".join([title, nama])
        print(f"{index+1:3} | {nama:.15} | {waktu:.10} | {tanggal:.10} | {maskapai:.10}\n")

    ## Footer
    print("="*56)


def view_data_pemesan(nama, no_telp, email, maskapai, tagihan):
    nama = nama.replace(" ", "")
    no_telp = no_telp.replace(" ", "")
    email = email.replace(" ", "")
    maskapai = maskapai.replace(" ", "")
    tagihan = tagihan.replace(" ", "")

    os.system("clear")
    print("="*40)
    print("DATA PEMESAN".center(39))
    print("="*40+"\n")
    print(f"Nama     : {nama}\n")
    print(f"No.Telp  : {no_telp}\n")
    print(f"Email    : {email}\n")
    print(f"Maskapai : {maskapai}\n")
    print(f"Tagihan  : {tagihan}\n")
    print("="*40)


def view_data_penumpang(title, nama, tujuan, waktu, maskapai, tanggal):
    title = title.replace(" ", "")
    nama = nama.replace(" ", "")
    tujuan = tujuan.replace(" ", "")
    waktu = waktu.replace(" ", "")
    maskapai = maskapai.replace(" ", "")
    tanggal = tanggal.replace(" ", "")
    
    os.system("clear")
    print("="*40)
    print("DATA PENUMPANG".center(39))
    print("="*40+'\n')
    print(f"Title    : {title}\n")
    print(f"Nama     : {nama}\n")
    print(f"Tujuan   : {tujuan}\n")
    print(f"Tanggal  : {tanggal}\n")
    print(f"Waktu    : {waktu}\n")
    print(f"Maskapai : {maskapai}\n")
    print("="*40)


def update_pemesan(data):
    pk = data[0]
    nama = data[2]
    tgl_booking = data[1]
    no_telp = data[3]
    email = data[4]
    maskapai = data[5]
    tagihan = data[6]
    
    view_data_pemesan(nama, no_telp, email, maskapai, tagihan)

    print("\nOption\n1. nama\n2. No_telp\n3. email\n")
    user_option = input("Pilih Data Yang Ingin Diubah[1,2,3]\t: ")

    match user_option:
        case "1": nama = input("Masukkan Nama\t: ")
        case "2": no_telp = input("Masukkan No.Telp\t: ")
        case "3": email = input("Masukkan Email\t: ")

    os.system("clear")
    print("="*40)
    print("DATA BARU ANDA".center(39))
    print("="*40+"\n")
    print(f"Nama    : {nama}\n")
    print(f"No.Telp : {no_telp}\n")
    print(f"Email   : {email}\n")
    print("="*40)

    operasi.update_pemesan(pk, tgl_booking, nama, no_telp, email, maskapai, tagihan)
    x = input("")


def update_penumpang(data):
    pk = data[0]
    title = data[1]
    nama = data[2] 
    waktu = data[3]
    tanggal = data[4]
    maskapai = data[5]
    jurusan = data[6]

    view_data_penumpang(title, nama, jurusan, waktu, maskapai, tanggal)

    print("\nOption\n1. Title\n2. nama\n3. No_telp\n4. email\n")
    user_option = input("Pilih Data Yang Ingin Diubah[1,2,3,4]\t: ")
    print("")

    match user_option:
        case "1": title = input("Masukkan Title\t: ")
        case "2": nama = input("Masukkan Nama\t: ")
        case "3": waktu = input("Masukkan Waktu\t: ")
        
    os.system("clear")
    print("="*40)
    print("DATA BARU ANDA".center(39))
    print("="*40+"\n")
    print(f"Title   : {title}\n")
    print(f"Nama    : {nama}\n")
    print(f"Waktu   : {waktu}\n")
    print("="*40)

    operasi.update_penumpang(pk, title, nama, waktu, tanggal, maskapai, jurusan)
    x =input("")