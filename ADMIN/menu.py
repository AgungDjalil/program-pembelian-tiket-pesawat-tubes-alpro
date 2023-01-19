from . import view

def menu():
    print("SELAMAT DATANG DI PROGRAM".center(66))
    print("DATABASE BOOKING PESAWAT".center(66))
    print("=========================".center(66))

    print("1. Read Data")
    print("2. Search Data")
    print("3. Update Data") 
    print("4. Sort Data")
    print("5. Delete Data\n")
    

def opsi_n_DB(user_option):
    while True:
        pilih = input("Baca Database Pemesan/Penumpang\t: ")
        if pilih in ["pemesan","penumpang"] :
            view.read_data()
            match user_option:
                case "1" : view.read_console(pilih)
                case "2" : view.search_console(pilih)
                case "3" : view.update_console(pilih) 
                case "4" : view.sort_console(pilih)
                case "5" : view.delete_console(pilih)
        else:
            print("Pilihan Tidak Valid")        
 

    