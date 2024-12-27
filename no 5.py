usia = int(input("Masukkan usia: "))

if usia <= 5:
  kategori = "Balita"
elif usia <= 12:
  kategori = "Anak-anak"
elif usia <= 17:
  kategori = "Remaja"
elif usia <= 59:
  kategori = "Dewasa"
else:
  kategori = "Lansia"

print("Kategori usia:", kategori)