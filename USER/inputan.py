


def kota_asal():
    while True:
        dari = input("Kota Keberangkatan\t: ")
        if dari == "" or len(str(dari)) <= 4:
            print("Tolong masukkan kota keberangkatan")
        elif dari in ['jakarta', 'surabaya', 'yogyakarta', 'makassar', 'denpasar']:
            return dari
            break
        else:
            print("Kota tidak tersedia")


def kota_tujuan():
    while True:
        ke = input("kota Tujuan        \t: ")
        if ke == "" or len(str(ke)) <= 4:
            print("Masukkan kota tujuan")
        elif ke in ['jakarta', 'surabaya', 'yogyakarta', 'makassar', 'denpasar']:
            return ke
            break
        else:
            print("Kota tidak tersedia")


def tanggal_berangkat():
    while True:
        try:
            tanggal = int(input("Tanggal (1-31)         \t: "))
            if tanggal not in range(1, 32):
                print("\nTolong masukkan tanggal yang valid")
            else:
                return tanggal
                break

        except ValueError:
            print("Tolong masukkan dengan angka")


def bulan_berangkat():
    while True:
        try:
            bulan = int(input("Bulan (1-12)           \t: "))
            if bulan not in range(1, 13):
                print("Tolong masukkan bulan yang valid")
            else:
                return bulan
                break

        except ValueError():
            print("Masukkan bulan dengan angka")


def tahun():
    while True:
        try:
            tahun = int(input("Tahun                  \t: "))
            if len(str(tahun)) != 4 or tahun <= 2022:
                print("masukan tahun yang valid")
            else:
                return tahun
                break
        except ValueError:
            print("Masukkan tahun yang valid")


def jumlah_dewasa():
    while True:  
        try:
            penumpang_dewasa = int(input("Dewasa              \t: "))
            if penumpang_dewasa >= 6:
                print("Maksimal penumpang 6 orang")
            else:
                return penumpang_dewasa
                break
        except ValueError:
            print("\nMasukkan Dengan Angka")


def jumlah_anak():
    while True:          
        try:
            penumpang_anak = int(input("Anak                \t: "))
            if penumpang_anak >= 3:
                print("Tidak bisa banyak anak")
            else:
                return penumpang_anak
                break
        except ValueError:
            print("Masukkan Dengan Angka")


def jumlah_infant():
    while True:
            try:
                penumpang_bayi = int(input("Bayi                \t: "))
                if penumpang_bayi >= 2:
                    print("Terlalu banyak bayi")
                else:
                    return penumpang_bayi
                    break
            except ValueError:
                print("Masukkan Dengan Angka")


def pesan():
    while True:
        print("Frequently Added to Booking")
        asuransi_perjalanan = input("◽ Travel Asuransi Rp 37.000/pax? (ya/tidak) : ")
        print("")

        if asuransi_perjalanan == "ya":
            asuransi = 37000
            return asuransi
            break
        elif asuransi_perjalanan == "tidak":
            asuransi = 0
            return asuransi
            break
        else:
            print ("Please try again")


def data_pemesan():
    print("Contact Details (for E-ticket/Voucher)")
    while True:
        nama = input("◾ Nama Lengkap    \t: ")
        if nama == "":
            print("\nTolong masukkan nama")
        else:
            break    

    while True:        
        nomor = input("◾ Nomor Handphone \t: +62 ")
        if nomor == "":
            print("Masukkan Nomor Telephone")
        else:
            try:
                nomor = int(nomor)
                if len(str(nomor)) == 11:
                    break
                else:
                    print("Masukkan Dengan 11 Digit Angka")
            except ValueError:
                print("Masukkan dengan angka")

    while True:            
        email = input("◾ Email           \t: ")
        if email == "":
            print ("Tolong masukan email addres")
        else:
            break  
    
    pemesan = f"{nama},{nomor},{email}"
    return pemesan
    

def title():
    while True:
        title = input("◾ Title (Mr/Ms) : ")
        if title not in ['Mr', 'Mrs', 'Ms']:
            print("Pilihan Tidak Valid")
        elif title == "":
            print("Masukkan title")
        else:
            return title
            break


def nama_depan():
    while True:
        first_name = input("◾ First Name              : ")
        if first_name == "":
            print("Please enter the name of passenger")
        else:
            return first_name           
            break
        

def nama_belakang():
    while True:
        last_name = input("◾ Last Name              : ")
        if last_name == "":
            print("Please enter the name of passenger")
        else:
            return last_name
            break