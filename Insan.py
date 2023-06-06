class Insan:
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk):#Insan sınıfının yapıcı metodu.
        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk

    def get_tc_no(self):#İnsanın TC kimlik numarasını döndüren bir get metodu.
        return self.__tc_no

    def set_tc_no(self, tc_no):#İnsanın TC kimlik numarasını ayarlayan bir set metodu.
        self.__tc_no = tc_no

    def get_ad(self):#İnsanın adını döndüren bir get metodu.
        return self.__ad

    def set_ad(self, ad):#İnsanın adını ayarlayan bir set metodu.
        self.__ad = ad

    def get_soyad(self):#İnsanın soyadını döndüren bir get metodu.
        return self.__soyad

    def set_soyad(self, soyad):#İnsanın soyadını ayarlayan bir set metodu.
        self.__soyad = soyad

    def get_yas(self):#İnsanın yaşını döndüren bir get metodu.
        return self.__yas

    def set_yas(self, yas):#İnsanın yaşını ayarlayan bir set metodu.
        self.__yas = yas

    def get_cinsiyet(self):#İnsanın cinsiyetini döndüren bir get metodu.
        return self.__cinsiyet

    def set_cinsiyet(self, cinsiyet):#İnsanın cinsiyetini ayarlayan bir set metodu.
        self.__cinsiyet = cinsiyet

    def get_uyruk(self):#İnsanın uyruk bilgisini döndüren bir get metodu.
        return self.__uyruk

    def set_uyruk(self, uyruk):#İnsanın uyruk bilgisini ayarlayan bir set metodu.
        self.__uyruk = uyruk

    def __str__(self):#Insan nesnesinin bir dize temsili.
        return f"TC:{self.__tc_no},Ad: {self.__ad}, Soyad: {self.__soyad},Yaş:{self.__yas},Cinsiyet:{self.__cinsiyet},Uyruk:{self.__uyruk}"


