from Insan import Insan
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk,tecrubeler):# Issiz sınıfının yapıcı metodu.
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrubeler = {
            "mavi yaka": [],
            "beyaz yaka": [],
            "yönetici": []
        }
        self.__en_uygun_statu = ""

    def get_tecrubeler(self):#İşsizin tecrübelerini döndüren bir get metodu.
        return self.__tecrubeler

    def tecrube_ekle(self, statu, yil):#İşsizin tecrübe eklemesini yapan bir metot.
        if statu in self.__tecrubeler:
            self.__tecrubeler[statu].append(yil)

    def statu_bul(self):#İşsizin en uygun statüsünü belirleyen bir metot.
        try:
            mavi_yaka_etkisi = sum(self.__tecrubeler["mavi yaka"]) * 0.2
            beyaz_yaka_etkisi = sum(self.__tecrubeler["beyaz yaka"]) * 0.35
            yonetici_etkisi = sum(self.__tecrubeler["yönetici"]) * 0.45

            en_yuksek_etki = max(mavi_yaka_etkisi, beyaz_yaka_etkisi, yonetici_etkisi)

            if en_yuksek_etki == mavi_yaka_etkisi:
                self.__en_uygun_statu = "mavi yaka"
            elif en_yuksek_etki == beyaz_yaka_etkisi:
                self.__en_uygun_statu = "beyaz yaka"
            else:
                self.__en_uygun_statu = "yönetici"
        except:
            print("Geçerli bir hesaplama yapılamadı.")

    def get_en_uygun_statu(self):#İşsizin en uygun statüsünü döndüren bir get metodu.
        return self.__en_uygun_statu

    def __str__(self):# Issiz nesnesinin bir dize temsili.
        self.statu_bul()
        return f"{super().__str__()}, En Uygun Statü: {self.get_en_uygun_statu()}"



