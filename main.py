"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 2 Desember 2022
    Waktu: 15:55:17 WIB
    Magnitudo: 4.9
    Kedalaman: 126 km
    Lokasi: LS=0.14 LS  BT=123.25
    Pusat Gempa: Pusat gempa berada dilaut 103 Km Timur Laut Salakan
    Dirasakan: Dirasakan (Skala MMI): II-III Banggai Laut
    :return: 
    """
    hasil = dict()
    hasil['tanggal'] = '2 Desember 2022'
    hasil['waktu'] = '15:55:17 WIB'
    hasil['magnitudo'] = 4.9
    hasil['lokasi'] = {'ls': 0.14, 'bt': 123.25}
    hasil['pusat'] = 'Pusat gempa berada dilaut 103 Km Timur Laut Salakan'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II-III Banggai Laut'

    print(hasil)
    return hasil

def tampilkan_data(result):
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")

if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
