import pandas as pd
import openpyxl

dataFrame = pd.read_csv("../other/data.jabarprov.go.id/disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.csv")

# 1.tampilkan data
dataFrame.head()
print(dataFrame)
dataFrame.to_csv("dataSampahJabar.csv", index=False)

dataFrame.to_excel("dataSampahJabar.xlsx", index=False)
# 2.hitunglah total produksi sampah di seluruh Kabupaten/Kota di Jawa Barat untuk tahun tertentu.no
def no2():
    tahun = int(input("masukan tahun(2015-2023)"))
    totalProduksi = 0
    for i, j in dataFrame.iterrows():
        if j["tahun"] == tahun:
            totalProduksi = totalProduksi + j["jumlah_produksi_sampah"]
        
    print(f"Total produksi sampah di seluruh Kabupaten/Kota Jawa Barat untuk tahun {tahun}: {totalProduksi} TON PER HARI")

    dfNo2 = pd.DataFrame({"tahun": [tahun], "total_produksi_sampah": [totalProduksi]})
    dfNo2.to_csv("tahunTertentu.csv", index=False)
    dfNo2.to_excel("tahunTertentu.xlsx", index=False)


# 3.Jumlahkan Data Pertahun
def no3():
    listTahun = {2015: [], 2016: [], 2017: [], 2018: [], 2019: [], 2020: [], 2021: [], 2022: [], 2023: []}

    tahun = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

    for i, j in dataFrame.iterrows():
        for x in tahun:
            if j["tahun"] == x:
                listTahun[x].append(j["jumlah_produksi_sampah"])
                break

    for i in tahun:
        print(f"total jumlah sampah pada tahun {i} adalah: {sum(listTahun[i])}")

    dfno3 = pd.DataFrame(listTahun.items(), columns=["tahun", "total_produksi_sampah"])
    dfno3.to_csv("totalPerTahun.csv", index=False)
    dfno3.to_excel("totalPerTahun.xlsx", index=False)

# 4.Jumlahkan data per Kota/Kabupaten per tahun
def no4():
    dictData= {}

    for i, j in dataFrame.iterrows():
        key = (j['nama_kabupaten_kota'], j['tahun'])
        dictData[key] = 0

    for i, j in dataFrame.iterrows():
        key = (j['nama_kabupaten_kota'], j['tahun'])
        dictData[key] += j['jumlah_produksi_sampah']

    print("Jumlah produksi sampah per Kota/Kabupaten per tahun:")
    rows = []
    for (kabupaten, tahun), sampah in dictData.items():
        print(f"{kabupaten} - {tahun}: {sampah} TON PER HARI")
        rows.append({"nama_kabupaten_kota": kabupaten, "tahun": tahun, "jumlah_produksi_sampah": sampah})

    dfno4 = pd.DataFrame(rows)
    dfno4.to_csv("totalPerKota.csv", index=False)
    dfno4.to_excel("totalPerKota.xlsx", index=False)

print("soal no 2")
no2()
print()
print("soal no 3")
no3()
print()
print("soal no 4")
no4()