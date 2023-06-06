from Calisan import Calisan
class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):#Yıpranma payı değerini döndüren bir get metodu.
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):#Yıpranma payı değerini ayarlayan bir set metodu.
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):#Çalışanın zam hakkını hesaplayan bir metot.
        try:
            if self.get_tecrube() < 2:
                return self.__yipranma_payi * 10
            elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
                return (self.get_maas() * self.get_tecrube() / 100) + (self.__yipranma_payi * 10)
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                return (self.get_maas() * self.get_tecrube() / 300) + (self.__yipranma_payi * 10)
            else:
                return self.get_maas()
        except ZeroDivisionError:
            return 0

    def __str__(self):#MaviYaka nesnesinin bir dize temsili.
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Tecrübe: {self.get_tecrube()}, Yeni Maaş: {self.zam_hakki()}"


