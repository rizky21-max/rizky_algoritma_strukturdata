def tambah(a, b):
  return a + b

def kurang(a, b):
  return a - b

def kali(a, b):
  return a * b

def bagi(a, b):
  if b == 0:
    return "Tidak dapat dibagi dengan nol"
  else:
    return a / b

# Contoh penggunaan
print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = int(input("Masukkan pilihan: "))
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == 1:
  hasil = tambah(angka1, angka2)
elif pilihan == 2:
  hasil = kurang(angka1, angka2)
elif pilihan == 3:
  hasil = kali(angka1, angka2)
elif pilihan == 4:
  hasil = bagi(angka1, angka2)
else:
  print("Pilihan tidak valid")

print("Hasil:", hasil)