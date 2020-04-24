import class1
import sys

def error():
    print("\n!!Anda telah memilih inputan yang salah!!")
    return 0

def non_return_func(praktikan1, praktikan2):
    print(f"{praktikan1} - 21120119140120 dan {praktikan2} - 21120119140145")
    print('Shift 2 - Kelompok 53\n\n')

   #Pemanggilan identitas
non_return_func("Abimanyu Putro Yulianto", "Elmar Leonard")

    #Judul
print('---------E&A Jacket---------\n\n')

hoodie = ["Jeans", "Hoodie", "Kulit"]
harga = [350000, 250000, 450000]
print("Daftar jenis jaket yang kami jual :")
i = 0
while i < 3:
    print("{}. Jaket".format(i+1), hoodie[i], " - Rp.", harga[i])
    i += 1
pil = int(input("Pilih jenis jaket yang anda inginkan = "))
if (0 < pil < 4):
    x = 1
    p1 = class1.kelas(x, hoodie, harga, pil)
    ukuran = ["M", "L", "XL", "XXL"]
    print("\nDaftar ukuran jaket yang tersedia :")
    for i in range(4):
        print("{}.".format(i+1), ukuran[i])
    pil1 = int(input("Pilih ukuran jaket yang anda inginkan = "))
    if (0 < pil1 < 5):
        y = 2
        p1.hasil(y, hoodie, ukuran, harga, pil1, pil)
    elif (pil1 <= 0):
        error()
        sys.exit(0)
    else :
       error()
       sys.exit(0)
elif(pil <= 0):
    error()
else :
    error()
    sys.exit(0)

j = int(input("\nMasukan jumlah yang anda inginkan : "))
h = j*harga[pil-1]
print("\nTerima kasih telah membeli", j, "pakaian")
print("Dengan total harga Rp.", h)