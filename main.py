import os
import USER as USER
import ADMIN as ADMIN


if __name__ == "__main__":
    os.system("clear")
    x = input(" ")

    if x == "admin":
        USER.loading()
        while(True):
            
            ADMIN.view_menu()

            user_option = input("Masukan opsi: ")
            
            if user_option == "1":
                pilih = input("Baca Database Pemesan/Penumpang: ")
                ADMIN.read_console(pilih)
            elif user_option == "2":
                pilih = input("Search Database Pemesan/Penumpang: ")
                ADMIN.search_console(pilih)


            is_done = input("\nApakah Selesai (y/n)? ")
            if is_done == "y" or is_done == "Y":
                break
    else:
        while True:
            USER.loading()

            print("==================================".center(66))
            print(" TRAVELOKE 🛫 BOOK FLIGHT TICKET ".center(66))
            print("==================================".center(66))
            print("")

            USER.kota()
            USER.buat_data()

            inputuser = input("\n\nKembali Ke Menu? (y/n)")
            if inputuser == "n":
                break
