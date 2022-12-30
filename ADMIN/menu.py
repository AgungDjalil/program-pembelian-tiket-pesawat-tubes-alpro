from . import operasi
from . import view

def view_menu():
    print("SELAMAT DATANG DI PROGRAM".center(66))
    print("DATABASE BOOKING PESAWAT".center(66))
    print("=========================".center(66))

    print("1. Read Data")
    print("2. Search Data")
    print("3. Delete Data") 
    print("4. Update Data\n")
 

def read_console(pilih):
    pilih.lower()
    pilihan = "".join(["data", pilih])
   
    data_file = operasi.read(pilihan)

    if pilih == "pemesan":
        view.pemesan_data(data_file)
    elif pilih == "penumpang":
        view.penumpang_data(data_file)   

         
def search_console(pilih):
    pilih.lower()
    read_console(pilih)
    print("")
    while(True):
        print("Menu Search Data".center(70))
        print("\n1. Cari Berdasarkan Nomor\n2. Cari Berdasarkan pk")

        pencarian_data = input("Masukkan Opsi\t: ")
        
        if pencarian_data == "1" and pilih == "pemesan":
            while(True):
                no_data = int(input("Masukkan Nomor Data\t: "))
                data_pemesan = operasi.search_data_pemesan(index=no_data)
                if data_pemesan:
                    break
                else:
                    print("Nomor Tidak Valid")


            data_break = data_pemesan.split(",")
            pk = data_break[0]
            tanggal = data_break[1]
            nama = data_break[2]
            nomor = data_break[3]
            email = data_break[4]
            maskapai = data_break[5]
            tagihan = data_break[6]
            operasi.satu_pemesan(pk, tanggal, nama, nomor, email, maskapai, tagihan)




