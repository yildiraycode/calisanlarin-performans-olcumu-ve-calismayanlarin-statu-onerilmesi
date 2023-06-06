from Insan import Insan
class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas

    def get_sektor(self):#Çalışanın sektor değerini döndüren bir get metodu.
        return self.__sektor

    def set_sektor(self, sektor):#Çalışanın sektor değerini ayarlayan bir set metodu.
        self.__sektor = sektor

    def get_tecrube(self):#Çalışanın tecrube değerini döndüren bir get metodu.
        return self.__tecrube

    def set_tecrube(self, tecrube):#Çalışanın tecrube değerini ayarlayan bir set metodu.
        self.__tecrube = tecrube

    def get_maas(self):#Çalışanın maas değerini döndüren bir get metodu.
        return self.__maas

    def set_maas(self, maas):#Çalışanın maas değerini ayarlayan bir set metodu.
        self.__maas = maas

    def zam_hakki(self):#Çalışanın zam hakkını hesaplayan bir metot.
        try:
            if self.__tecrube < 2:
                return 0
            elif 2 <= self.__tecrube <= 4 and self.__maas < 15000:
                return (self.__maas * self.__tecrube) / 100
            elif self.__tecrube > 4 and self.__maas < 25000:
                return (self.__maas * self.__tecrube) / 200
            else:
                return self.__maas
        except ZeroDivisionError:
            return 0

    def __str__(self):#Calisan nesnesinin bir dize temsili.
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Tecrübe: {self.get_tecrube()}, Yeni Maaş: {self.zam_hakki()}"


