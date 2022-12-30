

def pemesan_data(data_file):
    ## header
    tanggal = "TANGGAL"
    nama = "NAMA"
    nomor = "NOMOR TELP"
    email = "EMAIL"
    tagihan = "TAGIHAN"

    print("="*56)
    print(f"{tanggal:15} | {nama:20} | {nomor:10} | {tagihan:10}")
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