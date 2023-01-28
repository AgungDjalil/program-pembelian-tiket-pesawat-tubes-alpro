import os,sys 

DB_PEMESAN = "datapemesan.txt"
DB_PENUMPANG = "datapenumpang.txt"

os.getcwd()
new_dir = os.getcwd()
PATH =  new_dir

TEMPLATE_DATA_PEMESAN = {
    "pk": "xxxxxxxxxx",
    "tanggal_booking": "yyyy-mm-dd",
    "nama": 222*" ",
    "nomor": 255*" ",
    "email": 255*" ",
    "maskapai": 255*" ",
    "tagihan": 255*" "
}

TEMPLATE_DATA_PENUMPANG = {
    "pk": "xxxxxxxxxx",
    "title": "XX",
    "nama": 255*" ",
    "waktu": 255*" ",
    "tanggal": 100*" ",
    "jurusan": 255*" ",
    "maskapai": 255*" "
}