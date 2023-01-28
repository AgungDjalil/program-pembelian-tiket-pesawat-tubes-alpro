import os
import USER as USER
import ADMIN as ADMIN


if __name__ == "__main__":

    while True:
        os.system("clear")
        print("Selamat Datang Di Program".center(90))
        x = input(" ")

        if x == "admin":
            while True:
                ADMIN.menu()
                user_option = input("Masukan opsi: ")
                if user_option in ["1", "2", "3", "4", "5"]:
                    ADMIN.opsi_n_DB(user_option)
                elif user_option == "6":
                    break
                else:
                    print("Pilihan Tidak Valid")


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
