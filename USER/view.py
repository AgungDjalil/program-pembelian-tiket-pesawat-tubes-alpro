import csv, os
from . import operasi
import math
from . import inputan
from .operasi import loading

def kota():
    print("""
                            Pilih Kota
           =========================================
           |    Keberangkatan   |    Kedatangan    |
           =========================================
           |   ▶Jakarta         |    ▶Jakarta      |
           |   ▶Makassar        |    ▶Makassar     |
           |   ▶Surabaya        |    ▶Surabaya     |
           |   ▶Yogyakarta      |    ▶Yogyakarta   |
           |   ▶Denpasar        |    ▶Denpasar     |
           =========================================
    """)


def buat_data():
    while(True):
        dari = inputan.kota_asal()
        
        ke = inputan.kota_tujuan()

        if dari != ke:
            break
        else:
            print("kota Tujuan dan Keberangkatan Tidak Boleh Sama")

    print("\nTanggal Keberangkatan")
    tanggal = inputan.tanggal_berangkat()

    print("\nBulan Keberangkatan")
    bulan = inputan.bulan_berangkat()

    print("\nTahun Keberangkatan")
    tahun = inputan.tahun()

    print("\nMasukkan Jumlah Penumpang")
    dewasa = inputan.jumlah_dewasa()

    anak = inputan.jumlah_anak()

    bayi = inputan.jumlah_infant()

    loading()
    
    ## Melihat Dan Mengambil Data Pesawat
    pesawat = lihat_jadwal(dari, ke)
    data_break = pesawat.split(",")
    maskapai = data_break[0]
    waktu = data_break[1]
    harga = int(data_break[2])

    ## Perhitungan Potongan Harga dan Asuransi
    harga_dewasa = operasi.untuk_dewasa(dewasa, harga)
    harga_anak = operasi.untuk_anak(anak, harga)
    harga_bayi = operasi.untuk_bayi(bayi, harga)
    asuransi = inputan.pesan()

    ## Perhitungan Harga Keseluruhan
    total_penumpang = dewasa + anak + bayi
    total_harga = harga_dewasa + harga_anak + harga_bayi + asuransi
    original = math.ceil((harga_dewasa + harga_anak + harga_bayi) * harga)
    insurance = math.ceil((harga_dewasa + harga_anak + harga_bayi) * asuransi)

    ## User Mengisi Data Diri Pemesan
    data_pemesan = inputan.data_pemesan()
    data_pisah = data_pemesan.split(",")
    nama_pemesan = data_pisah[0]
    nomor_pemesan = data_pisah[1]
    email_pemesan = data_pisah[2]

    ## Operasi Data Pemesan Disimpan Ke Database 
    operasi.database_pemesan(maskapai, data_pemesan, total_harga)

    thn_tgl_bln = f'{tahun}-{tanggal}-{bulan}'  

    loading()

    ## Operasi Data Penumpang Disimpan Ke Database
    jurusan = dari + '->'+ ke
    data_utuh = operasi.data_penumpang(total_penumpang, thn_tgl_bln, waktu, maskapai, jurusan)

    loading()

    ## Tampilan Akhir
    flight_detail(maskapai, dari, ke, tanggal, bulan, tahun, nama_pemesan, nomor_pemesan, email_pemesan, data_utuh, total_harga, original, insurance, waktu)
    

def flight_detail(maskapai, dari, ke, tanggal, bulan, tahun, nama_pemesan, nomor_pemesan, email_pemesan, data_utuh, total_harga, original, insurance, waktu):
    print("============  FLIGHT DETAILS  ============")
    print("Please make sure that all information \nwritten below are correct")
    print("")
    print(maskapai)
    print("🛫", dari, "\t  {}/{}/{}". format(tanggal, bulan, tahun))
    print(" | ", waktu)
    print(" | ")
    print(" | ")
    print("🛬", ke)
    print(f"{waktu}")
    print("")
    print("CONTACT DETAILS")
    print(f"◾ Full Name     : {nama_pemesan}")
    print(f"◾ Mobile Number :  +62{nomor_pemesan}" )
    print(f"◾ Email         : {email_pemesan}")
    print("\nPASSENGER DETAILS")
    dataTraveller(data_utuh)
    print("\nPRICE DETAILS")
    print("◾ Price You Pay         : Rp", total_harga)
    print("◾ Total Original Price  : Rp ", original)
    print("◾ Insurance             : Rp ", insurance)
    print("")
    print("We will send your booking confirmations to the above contact details,\nwhich will also be used for refund or reschedule purposes.")


def lihat_jadwal(dari, ke):
    ## Operasi Mencari Dan Menampilkan Jurusan
    kota = "_".join([dari, ke])
    data_file = operasi.read(kota)

    ## Header
    no = "NO"
    airlines = "AIRLINES"
    time = "TIME"
    price = "PRICE"
    print("=" * 56)
    print(f"{no:2} | {airlines:15} | {time:15} | {price:15}")
    print("-" * 56)

    ## content
    for index,data in enumerate(data_file):
        if index == 0:
            pass
        else:
            data_break = data.split(",")
            no = data_break[0]
            airlines = data_break[1]
            time = data_break[2]
            price = int(data_break[3])
        
            print(f"{no:2} | {airlines:15} | {time:15} | {price:15,.2f}")
    
    ## Footer
    print("=" * 56)
    
    no_pesawat = input("No Pesawat: ")
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        no = data_break[0]
        airlines = data_break[1]
        time = data_break[2]
        price = data_break[3]

        if no == no_pesawat:
            loading()
            pesawat_pilihan = f"{airlines}, {time}, {price}"
            print(f'airlines : {airlines}')
            print(f'time     : {time}')
            print(f'price    : {price}')
            return pesawat_pilihan
            break
        

def dataTraveller(data_utuh):
    n = 0
    for data in data_utuh:
        n += 1
        print(f"◾ Passenger {n} : {data}")
