from Calisan import Calisan
class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):#Tesvik primi değerini döndüren bir get metodu.
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):#Tesvik primi değerini ayarlayan bir set metodu.
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):#Çalışanın zam hakkını hesaplayan bir metot.
        try:
            if self.get_tecrube() < 2:
                return self.__tesvik_primi * 1000
            elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
                return (self.get_maas() * self.get_tecrube() / 200) + (self.__tesvik_primi * 1000)
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                return (self.get_maas() * self.get_tecrube() / 400) + (self.__tesvik_primi * 1000)
            else:
                return self.get_maas()
        except ZeroDivisionError:
            return 0

    def __str__(self):#BeyazYaka nesnesinin bir dize temsili.
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Tecrübe: {self.get_tecrube()}, Yeni Maaş: {self.zam_hakki()}"

