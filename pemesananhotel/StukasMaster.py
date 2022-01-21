#Import Library
from operator import index
import pandas as pd
import datetime as dt

#Definisi Variabel
listHotel = [
    {
        "Hotel Skylone":
            {"Jenis Kamar" : 
                {"Single Room":
                    {"Harga":350000,
                    "Fasilitas":"\nA. Free WiFi\nB. 1 King Bed\nC. Shower"},
                "Family Room":
                    {"Harga":500000,"Fasilitas":"\nA. Free WiFi\nB. 1 King Bed\nC. 1 Single Bed\nD. Shower"}
            },
            "Charge" :
                {
                    "Breakfast":100000,
                    "Lunch":100000,
                    "Dinner":150000,
                    "Fitness":120000
                }
            
            }
    },
    {    
        "Hotel Hilton":{
            "Jenis Kamar":
                {"Single Room":
                    {"Harga":400000,
                    "Fasilitas":"\nA. Free WiFi\nB. 1 King Bed\nC. Bathup"},
                "Family Room":
                {"Harga":650000,
                "Fasilitas":"\nA. Free WiFi\nB. 1 King Bed\nC. 1 Single Bed\nD. Bathup"}
                },
            "Charge" :
                {
                    "Breakfast" : 170000 ,
                    "Fitness" : 150000,
                    "Sauna" : 150000,
                }
            }
            },
    {   
         "Hotel Pialepasa": {
            "Jenis Kamar":
                {"Single Room":
                    {"Harga":375000,"Fasilitas":"\nA. Saluran TV Premium\nB. 1 King Bed\nC. Shower"},
                "Family Room":
                    {"Harga":450000,"Fasilitas":"\nA. Saluran TV Premium\nB. 1 King Bed\nC. 1 Single Bed\nD. Shower"}
                },
            "Charge":
                {
                    "Breakfast":100000,
                    "Lunch":100000,
                    "Fitness":175000
            }
            }
            },
    {   
         "Hotel Menalo": {
            "Jenis Kamar":
                {"Single Room":
                    {"Harga":350000,"Fasilitas":"\nA. Free WiFi\nB. 1 King Bed\nC. Shower\nD. Swimming pool"},
                "Family Room":
                    {"Harga":550000,"Fasilitas":"\nA. Free WiFi\nB. 1 King Bed\nC. 1 Single Bed\nD. Shower\n5. Swimming pool"}
                },
            "Charge":
                {
                    "Breakfast" : 100000,
                    "Sauna" : 150000,
                    "Salon" : 125000,
                    "Fitness" : 150000
                }
            }
    }       
]
hotelTerpilih=[]
kamarTerpilih=[]
hargaKamar=[]
chargeTerpilih=[]
tagihanCharge=[]
lamaMenginap=[]
totalTagihanKamar=[]
listCharge=[]

waktuSekarang = dt.datetime.now()
i=0
listLogin =['admin-admin123']


print("Selamat Datang Di BALI TRAVELOKAL")
print("="*40)
print("Silahkan Login Untuk Melanjutkan Akses")

#LOGIN
username=input("Masukkan Username Anda : ")
password=input("Masukan Password Anda : ")
login = username +"-"+password

#Cek apakah login Valid
while login not in listLogin:
    print("Masukan Username dan Password yang Valid !")
    username=input("Masukkan Username Anda : ")
    password=input("Masukan Password Anda : ")
    login = username +"-"+password
else:
    print("Login Berhasil\n")
    print("="*40)

#Menampilkan Daftar Hotel Tersedia
print("Daftar Hotel Tersedia di BALI TRAVELOKAL")
for item in listHotel:
    for hotel in item :
        i+=1
        print(i,hotel)
#Menginput Hotel yang dipilih
pilihHotel = int(input("Masukan Kode Hotel : "))

#Validasi apakah memilih hotel sesuai
while pilihHotel>4 or pilihHotel<1:
    print("Silahkan Input Kode yang Valid : ")
    pilihHotel = int(input("Masukan Kode Hotel"))

#menampilkan detail hotel
for namaHotel,jenisKamar in listHotel[pilihHotel-1].items():
    print("Jenis Kamar di",namaHotel)
    hotelTerpilih.append(namaHotel)
    i=0
    for opsiKamar,deskripsi in jenisKamar["Jenis Kamar"].items():
        i+=1
        print("\n{} {}".format(i,opsiKamar))
        for item,keterangan in deskripsi.items():
            print(item,":",keterangan)
    print("\nCharge")
    for jenisCharge,biaya in jenisKamar["Charge"].items():
        print(jenisCharge,":",biaya)

#Menginput Kamar yang diinginkan
pilihKamar = input("Pilih Jenis Kamar yang Anda Mau (1/2) : ")
if pilihKamar =="1":
    kamarTerpilih.append("Single Room")
elif pilihKamar == "2":
    kamarTerpilih.append("Family Room")
biayaKamar=listHotel[pilihHotel-1][namaHotel]["Jenis Kamar"][kamarTerpilih[0]]["Harga"]
chargeHotel=listHotel[pilihHotel-1][namaHotel]["Charge"]

#Menmilih Tambahan Charge Hotel
pilihCharge = input("Apakah Akan Menambah Charge ? (yes/no) : ").lower()
if pilihCharge == "yes":
    charge = input("Masukan Jenis Charge yang diinginkan : ").capitalize()
    biayaCharge = chargeHotel[charge]
    tagihanCharge.append(biayaCharge)
    chargeTerpilih.append(charge)
    newDict = {"Charge":charge , "Biaya":biayaCharge}
    listCharge.append(newDict)
    decision1= input("Apakah ingin menambah lagi ? (yes/no) : ").lower()
    while decision1 == "yes":
        charge = input("Masukan Jenis Charge yang diinginkan : ").capitalize()
        if charge in chargeTerpilih:
            print("Anda Telah Memilih Jenis Charge Tersebut")
            continue
        biayaCharge = chargeHotel[charge]
        tagihanCharge.append(biayaCharge)
        chargeTerpilih.append(charge)
        newDict = {"Charge":charge , "Biaya":biayaCharge}
        listCharge.append(newDict)
        decision1= input("Apakah ingin menambah lagi ? (yes/no) : ").lower()

#Menginput Tanggal CheckIN
checkIn = input("Masukan Tanggal Check In (yyyy-mm-dd) : ")
tanggalCheckIn = dt.datetime.strptime(checkIn, "%Y-%m-%d")

#Menginput Lama Hari Menginap
menginap = int(input("Berapa lama anda akan menginap ? : "))
totalBiayaKamar = biayaKamar*menginap
lamaMenginap.append(menginap)
totalTagihanKamar.append(totalBiayaKamar) 
tanggalCheckOut = tanggalCheckIn + dt.timedelta(menginap)
df_invoice={
            'Extra Charge':chargeTerpilih,
            'Biaya Charge':tagihanCharge, 
        }
grandTotal = sum(tagihanCharge) + totalBiayaKamar


#Menampilkan Output Detail Pemesanan
invoice=pd.DataFrame(data=df_invoice)
invoice.index+=1
print("="*50)
print(" "*10,"Detail Pemesanan Kamar")
print("="*50)
print("Nama Hotel \t\t:",namaHotel)
print("Lama Menginap \t\t:",menginap)
print("Tanggal CheckIN\t\t:",tanggalCheckIn.date())
print("Tanggal CheckOUT\t:",tanggalCheckOut.date())
if len(chargeTerpilih) >0:
    print("Transaksi\t: ")
    print(invoice.to_string(index=True))
    print("SubTotal Charge\t\t:",sum(tagihanCharge))
print("SubTotal Kamar\t\t:",totalBiayaKamar)
print("Grand Total\t\t:",totalBiayaKamar+sum(tagihanCharge))
print("="*50)