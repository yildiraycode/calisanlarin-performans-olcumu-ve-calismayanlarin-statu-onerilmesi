from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
import pandas as pd

def main():
    try:
        # İnsan nesnelerini oluştur
        insan1 = Insan("12345678910", "Ahmet", "Yılmaz", 30, "Erkek", "Türk")
        insan2 = Insan("98765432100", "Ayşe", "Demir", 25, "Kadın", "Türk")

        print(insan1)
        print(insan2)
        # # İşsiz nesnelerini oluştur
        issiz1 = Issiz("12345678910", "Ali", "Kaya", 28, "Erkek", "Türk", {"mavi yaka": 3, "beyaz yaka": 5, "yönetici": 10})
        issiz2 = Issiz("98765432100", "Fatma", "Çelik", 35, "Kadın", "Türk", {"mavi yaka": 2, "beyaz yaka": 4, "yönetici": 7})
        issiz3 = Issiz("55555555555", "Mehmet", "Öztürk", 40, "Erkek", "Türk", {"mavi yaka": 1, "beyaz yaka": 3, "yönetici": 5})

        print(issiz1)
        print(issiz2)
        print(issiz3)
        ## Çalışan nesnelerini oluştur
        calisan1 = Calisan("12345678910", "Ayşe", "Yıldız", 32, "Kadın", "Türk", "teknoloji", 24, 20000)
        calisan2 = Calisan("98765432100", "Ahmet", "Demir", 28, "Erkek", "Türk", "muhasabe", 10, 15000)
        calisan3 = Calisan("55555555555", "Zeynep", "Kaya", 40, "Kadın", "Türk", "inşaat", 48, 30000)

        print(calisan1)
        print(calisan2)
        print(calisan3)
        ## MaviYaka nesnelerini oluştur
        maviyaka1 = MaviYaka("12345678910", "Ali", "Yılmaz", 30, "Erkek", "Türk", "teknoloji", 24, 20000, 0.2)
        maviyaka2 = MaviYaka("98765432100", "Ayşe", "Demir", 25, "Kadın", "Türk", "muhasabe", 12, 18000, 0.5)
        maviyaka3 = MaviYaka("55555555555", "Mehmet", "Öztürk", 35, "Erkek", "Türk", "diğer", 6, 12000, 0.3)

        print(maviyaka1)
        print(maviyaka2)
        print(maviyaka3)

        beyazyaka1 = BeyazYaka("12345678910", "Ayşe", "Yıldız", 32, "Kadın", "Türk", "teknoloji", 24, 20000, 500)
        beyazyaka2 = BeyazYaka("98765432100", "Ahmet", "Demir", 28, "Erkek", "Türk", "muhasabe", 10, 15000, 2500)
        beyazyaka3 = BeyazYaka("55555555555", "Zeynep", "Kaya", 40, "Kadın", "Türk", "inşaat", 48, 30000, 1000)

        print(beyazyaka1)
        print(beyazyaka2)
        print(beyazyaka3)

        # DataFrame oluşturma
        data = {
            "Nesne": ["İnsan", "İnsan", "İşsiz", "İşsiz", "İşsiz", "Çalışan", "Çalışan", "Çalışan",
                      "Mavi Yaka", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
            "Tc No": ["12345678910", "98765432100", "12345678910", "98765432100", "55555555555",
                      "12345678910", "98765432100", "55555555555", "12345678910", "98765432100",
                      "55555555555", "12345678910", "98765432100", "55555555555"],
            "Ad": ["Ahmet", "Ayşe", "Ali", "Fatma", "Mehmet", "Ayşe", "Ahmet", "Zeynep",
                   "Ali", "Ayşe", "Mehmet", "Ayşe", "Ahmet", "Zeynep"],
            "Soyad": ["Yılmaz", "Demir", "Kaya", "Çelik", "Öztürk", "Yıldız", "Demir", "Kaya",
                      "Yılmaz", "Demir", "Öztürk", "Yıldız", "Demir", "Kaya"],
            "Yaş": [30, 25, 28, 35, 40, 32, 28, 40, 30, 25, 35, 32, 28, 40],
            "Cinsiyet": ["Erkek", "Kadın", "Erkek", "Kadın", "Erkek", "Kadın", "Erkek", "Kadın",
                         "Erkek", "Kadın", "Erkek", "Kadın", "Erkek", "Kadın"],
            "Uyruk": ["Türk", "Türk", "Türk", "Türk", "Türk", "Türk", "Türk", "Türk",
                      "Türk", "Türk", "Türk", "Türk", "Türk", "Türk"],
            "Sektör": ["-", "-", "-", "-", "-", "teknoloji", "muhasabe", "inşaat",
                       "teknoloji", "muhasabe", "diğer", "teknoloji", "muhasabe", "inşaat"],
            "Tecrübe (Yıl)": [0, 0, 3, 2, 1, 24, 10, 48, 24, 10, 48, 24, 10, 48],
            "Maaş": [0, 0, 0, 0, 0, 20000, 15000, 30000, 20000, 15000, 30000, 20000, 15000, 30000],
            "Yıpranma Payı": [0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0.5, 0.2, 0, 0, 0],
            "Teşvik Prim": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 500, 2500, 1000],
            "Yeni Maaş": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        }

        df = pd.DataFrame(data)
        print(df)
        print()

        # a) Bazı değişken değerleri diğer nesneler için boş olabilir, DataFrame için bu değerleri 0 atama
        df = df.fillna(0)
        print(df)
        print()

        # b) Çalışan, mavi yaka ve beyaz yaka için gruplandırarak tecrübe ve yeni maaş ortalamalarını hesapla ve yazdır
        grouped = df.groupby("Nesne").agg({"Tecrübe (Yıl)": "mean", "Yeni Maaş": "mean"})
        print(grouped)
        print()

        # c) Maaşı 15000 TL üzerinde olanların toplam sayısını bul
        count_above_15000 = df[df["Maaş"] > 15000].shape[0]
        print("Maaşı 15000 TL üzerinde olanların toplam sayısı:", count_above_15000)
        print()

        # d) Yeni maaşa göre DataFrame'i küçükten büyüğe sırala ve yazdır
        sorted_df = df.sort_values("Yeni Maaş")
        print(sorted_df)
        print()

        # e) Tecrübesi 3 seneden fazla olan Beyaz yakalıları bul ve yazdır
        experienced_beyaz_yaka = df[(df["Nesne"] == "Beyaz Yaka") & (df["Tecrübe (Yıl)"] > 3)]
        print(experienced_beyaz_yaka)
        print()

        # f) Yeni maaşı 10000 TL üzerinde olanlar için 2-5 satır arası olanları tc_no ve yeni_maaş sütunlarını seçerek göster ve yazdır
        filtered_df = df[(df["Yeni Maaş"] > 10000)].iloc[2:5, [1, 12]]
        print(filtered_df)
        print()

        # g) Ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame elde et ve yazdır
        new_df = df[["Ad", "Soyad", "Sektör", "Yeni Maaş"]]
        print(new_df)

    except Exception as e:
        print("Bir hata oluştu:", str(e))


if __name__ == "__main__":#ana programın çalıştır
    main()
