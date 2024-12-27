def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
  total_jam = jam_kerja_per_hari * hari_kerja
  lembur = max(0, total_jam - (8 * hari_kerja))
  gaji_pokok = total_jam * tarif_per_jam
  gaji_lembur = lembur * 1.5 * tarif_per_jam
  total_gaji = gaji_pokok + gaji_lembur
  return total_gaji

# Contoh penggunaan
tarif_per_jam = float(input("Masukkan tarif per jam: "))
jam_kerja_per_hari = int(input("Masukkan jam kerja per hari: "))
hari_kerja = int(input("Masukkan jumlah hari kerja: "))

gaji = hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja)
print("Total gaji:", gaji)