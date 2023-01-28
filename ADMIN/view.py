from . import operasi
import os


def read_console(pilih):
    pilih.lower()
    pilihan = "".join(["data", pilih])

    data_file = operasi.read(pilihan)

    match pilih:
        case "pemesan": pemesan_data(read_biasa=data_file)
        case "penumpang": penumpang_data(read_biasa=data_file)


def search_console(pilih):
    operasi.loading()
    pilih.lower()
    pilihan = "".join(["data", pilih])
    print("")

    while (True):
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

    x = input("")


def update_console(pilih):
    operasi.loading()
    pilih.lower()
    pilihan = "".join(["data", pilih])
    print("")

    while (True):
        no_pk = str(input("Masukkan PK\t: "))
        data = operasi.search(no_pk, pilihan)
        if data:
            break
        else:
            print("No PK Tidak Valid, Masukkan sekali Lagi")

    match pilih:
        case "pemesan": update_pemesan(data)
        case "penumpang": update_penumpang(data)


def sort_console(pilih):
    operasi.loading()
    pilih.lower()
    pilihan = "".join(["data", pilih])
    print("")

    data = operasi.data_sort(nama_file=pilihan)
    match pilih:
        case "pemesan": pemesan_data(sorting=data)
        case "penumpang": penumpang_data(sorting=data)


def delete_console(pilih):
    operasi.loading()
    pilih.lower()
    pilihan = "".join(["data", pilih])

    while (True):
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
            case "pemesan": operasi.delete_pemesan(pk)
            case "penumpang": operasi.delete_penumpang(pk)


def pemesan_data(**data_file):
    if "read_biasa" in data_file: 
        os.system("clear")
        # header
        no = "NO"
        tanggal = "TANGGAL"
        nama = "NAMA"
        nomor = "NOMOR TELP"
        email = "EMAIL"
        tagihan = "TAGIHAN"

        print("="*72)
        print(f"{no:3} | {tanggal:10} | {nama:20} | {nomor:10} | {tagihan:15} |")
        print("-"*72)

        # content
        data_file = data_file["read_biasa"]
        for index, data in enumerate(data_file):
            data_break = data.split(",")
            pk = data_break[0]
            tanggal = data_break[1]
            nama = data_break[2]
            nomor = data_break[3]
            email = data_break[2]
            maskapai = data_break[5]
            tagihan = data_break[6]
            print(
                f"{index+1:3} | {tanggal:.10} | {nama:.20} | {nomor:.10} | {tagihan:.15} |")

        # footer
        print("="*72)

    else:
        os.system("clear")
        # header
        no = "NO"
        tanggal = "TANGGAL"
        nama = "NAMA"
        nomor = "NOMOR TELP"
        email = "EMAIL"
        tagihan = "TAGIHAN"

        print("="*72)
        print(f"{no:3} | {tanggal:10} | {nama:20} | {nomor:10} | {tagihan:15} |")
        print("-"*72)

        # content
        data_file = data_file["sorting"]
        for index, data in enumerate(data_file):
            pk = data[0]
            tanggal = data[1]
            nama = data[2]
            nomor = data[3]
            email = data[2]
            maskapai = data[5]
            tagihan = data[6]
            print(
                f"{index+1:3} | {tanggal:.10} | {nama:.20} | {nomor:.10} | {tagihan:.15} |")

        # footer
        print("="*72)
        
    x = input("")


def penumpang_data(**data_file):
    if "read_biasa" in data_file:
        os.system("clear")
        # Header
        no = "NO"
        nama = "NAMA"
        waktu = "WAKTU"
        tanggal = "TANGGAL"
        maskapai = "MASKAPAI"

        print("="*71)
        print(f"{no:2} | {nama:20} | {waktu:15} | {tanggal:10} | {maskapai:10} |")
        print("-"*71)

        # Content
        data_file = data_file["read_biasa"]
        for index, data in enumerate(data_file):
            data_break = data.split(",")
            title = data_break[1]
            nama = data_break[2]
            waktu = data_break[3]
            tanggal = data_break[4]
            maskapai = data_break[5]
            nama = " ".join([title, nama])
            print(
                f"{index+1:2} | {nama:.20} | {waktu:.15} | {tanggal:.10} | {maskapai:.10} |")

        # Footer
        print("="*71)
    else:
        os.system("clear")
        # Header
        no = "NO"
        nama = "NAMA"
        waktu = "WAKTU"
        tanggal = "TANGGAL"
        maskapai = "MASKAPAI"

        print("="*71)
        print(f"{no:2} | {nama:20} | {waktu:15} | {tanggal:10} | {maskapai:10} |")
        print("-"*71)

        # Content
        data_file = data_file["sorting"]
        for index, data in enumerate(data_file):
            title = data[1]
            nama = data[2]
            waktu = data[3]
            tanggal = data[4]
            maskapai = data[5]
            nama = " ".join([title, nama])
            print(
                f"{index+1:2} | {nama:.20} | {waktu:.15} | {tanggal:.10} | {maskapai:.10} |")

        # Footer
        print("="*71)

    x = input("")


def view_data_pemesan(nama, no_telp, email, maskapai, tagihan):
    nama = nama.strip()
    no_telp = no_telp.strip()
    email = email.strip()
    maskapai = maskapai.strip()
    tagihan = tagihan.strip().replace("\n", "")

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
    title = title.strip()
    nama = nama.strip()
    tujuan = tujuan.strip().replace("\n", "")
    waktu = waktu.strip()
    maskapai = maskapai.strip()
    tanggal = tanggal.strip()

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
        case "1": nama = input("Masukkan Nama\t: ").title()
        case "2": no_telp = input("Masukkan No.Telp\t: ")
        case "3": email = input("Masukkan Email\t: ")

    view_data_pemesan(nama, no_telp, email, maskapai, tagihan)

    operasi.update_pemesan(pk, tgl_booking, nama,
                           no_telp, email, maskapai, tagihan)
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
        case "1": title = input("Masukkan Title\t: ").title()
        case "2": nama = input("Masukkan Nama\t: ").title()
        case "3": waktu = input("Masukkan Waktu\t: ")

    view_data_penumpang(title, nama, jurusan, waktu, maskapai, tanggal)

    operasi.update_penumpang(pk, title, nama, waktu,
                             tanggal, maskapai, jurusan)
    x = input("")
