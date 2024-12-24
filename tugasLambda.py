import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../other/data.jabarprov.go.id/disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.csv")

def statusSampah(sampah):
    if sampah > 400:
        return "sampah harus segera ditanggulangi"
    else:
        return "sampah masil dalam kondisi aman"

def pajakSampah(status):
    if status == "sampah harus segera ditanggulangi":
        return 123000 * 0.05
    else:
        return 0
    

tahun = int(input("masukan tahun(2015-2023): "))

dfTahun = df[df['tahun'] == tahun]
dfGraph= dfTahun.sort_values(by='jumlah_produksi_sampah', ascending=True)


# 1.buat grafik untuk data tugas (data produksi sampah di jawa barat)
plt.figure(figsize=(10, 6))
plt.barh(dfGraph["nama_kabupaten_kota"], dfGraph["jumlah_produksi_sampah"], color="skyblue")
plt.title(f"Jumlah Produksi Sampah Berdasarkan Kabupaten/Kota ({tahun})")
plt.xlabel("Jumlah Produksi Sampah (Ton)")
plt.ylabel("Kabupaten/Kota")
plt.tight_layout()
plt.show()

#2.jumlahkan total sampah per kab/kota setiap tahun
totalSampah = df.groupby('nama_kabupaten_kota')["jumlah_produksi_sampah"].sum()
print(totalSampah.head(10))


#3.buat grafik berupa diagram batang horizontal / vertikal
plt.figure(figsize=(10, 6))
totalSampah.sort_values().plot(kind='barh', color='skyblue')
plt.title('Total Produksi Sampah per Kabupaten/Kota(2015-2023)')
plt.xlabel('jumlah produksi sampah(ton)')
plt.ylabel('kabupaten/kota')
plt.tight_layout()  
plt.show()

# 4. Buat kolom baru 'Kategori', buat if jika jumlah sampah lebih dari 400 ton maka sampah harus segera ditanggulangi sedangkan jika tidak, sampah masih dalam kategori aman
df["kategori"] = df["jumlah_produksi_sampah"].apply(statusSampah)
print(df.head(10))
# 5. hitung bayaran sampah dimana 1 ton harganya adalah 123.000
df["bayaran"] = df["jumlah_produksi_sampah"].apply(lambda x:x * 123000)
print(df.head(10))
# 6. hitung jika kategori sampah adalah  sampah harus segera ditanggulangi  maka tambahkan 1 kolom pajak yang berisi harga per ton dikali 5%
df["pajak"] = df["kategori"].apply(pajakSampah)
print(df.head(10))






