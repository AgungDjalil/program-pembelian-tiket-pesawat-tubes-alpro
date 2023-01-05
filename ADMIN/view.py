from . import operasi


def read_console(pilih):
    pilih.lower()
    pilihan = "".join(["data", pilih])
   
    data_file = operasi.read(pilihan)

    if pilih == "pemesan":
        pemesan_data(data_file)
    elif pilih == "penumpang":
        penumpang_data(data_file)  


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

    if pilih == "pemesan":
        update_pemesan(data)




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
    print("="*40)
    print("DATA PEMESAN".center(39))
    print("="*40)
    print(f"Nama     : {nama}")
    print(f"No.Telp  : {no_telp}")
    print(f"Email    : {email}")
    print(f"Maskapai : {maskapai}")
    print("")
    print(f"Tagihan  : {tagihan}")


def view_data_penumpang(title, nama, tujuan, waktu, maskapai, tanggal):
    print("="*40)
    print("DATA PENUMPANG".center(39))
    print("="*40)
    print(f"Title    : {title}")
    print("")
    print(f"Nama     : {nama}")
    print(f"Tujuan   : {tujuan}")
    print(f"Tanggal  : {tanggal}")
    print("")
    print(f"Waktu    : {waktu}")
    print("")
    print(f"Maskapai : {maskapai}")


def update_pemesan(data):
    pk = data[0]
    tgl_booking = data[1]
    nama = data[2]
    no_telp = data[3]
    email = data[4]
    maskapai = data[5]
    tagihan = data[6]

    while True:
        print("Option\n1. nama\n2. No_telp\n3. email\n")
        user_option = input("Pilih Data Yang Ingin Diubah[1,2,3]\t: ")

        if user_option == "1":
            nama = input("Masukkan Nama\t: ")
        elif user_option == "2":
            no_telp = input("Masukkan No.Telp\t:")
        elif user_option == "3":
            email = input("Masukkan Email\t: ")
        else:
            print("Pilihan Tidak Valid")
            pass

        print("Data Baru Anda")
        print(f"Nama    : {nama}")
        print(f"No.Telp : {no_telp}")
        print(f"Email   : {email}")
        
        keluar = input("Apakah Sudah (y/n)\t: ".lower())
        if keluar == "y":
            break

    operasi.update(pk, tgl_booking, nama, no_telp, email, maskapai, tagihan)
