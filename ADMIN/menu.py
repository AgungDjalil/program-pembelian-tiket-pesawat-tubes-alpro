from . import view


def menu():
    print("SELAMAT DATANG DI PROGRAM".center(66))
    print("DATABASE BOOKING PESAWAT".center(66))
    print("=========================".center(66))

    print("1. Read Data")
    print("2. Search Data")
    print("3. Delete Data") 
    print("4. Update Data\n")
    

def opsi_n_DB(user_option):
    if user_option == "1":
        pilih = input("Baca Database Pemesan/Penumpang\t: ")
        view.read_console(pilih)

    elif user_option == "2":
        pilih = input("Search Database Pemesan/Penumpang\t: ")
        view.search_console(pilih)

    elif user_option == "3":
        pilih = input("Search Database Pemesan/Penumpang\t: ")

    elif user_option == "4":
        pilih = input("Search Database Pemesan/Penumpang\t: ")


 

         





