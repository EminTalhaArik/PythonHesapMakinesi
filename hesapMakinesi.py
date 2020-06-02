# -*- coding: utf-8 -*-

def topla():
    
    sayi1 = int(input("Lütfen 1. Sayıyı Giriniz : "))
    sayi2 = int(input("Lütfen 2. Sayıyı Giriniz : "))
    
    sonuc = sayi1 + sayi2
    
    print(" ")
    print("Toplama İşleminizin Sonucu = " + str(sonuc)) 
    print(" ")
    
def cikar():
    
    sayi1 = int(input("Lütfen 1. Sayııy Giriniz : "))
    sayi2 = int(input("Lütfen 2. Sayıyı Giriniz : "))

    sonuc = sayi1 - sayi2
    
    print(" ")
    print("Çıkarma İşleminizin Sonucu = " + str(sonuc))
    print(" ")
    
def carp():
    
    sayi1 = int(input("Lütfen 1. Sayıyı Giriniz : "))
    sayi2 = int(input("Lütfen 2. Sayıyı Giriniz : "))
    
    sonuc = sayi1 * sayi2

    print(" ")
    print("Çarpma İşleminizin Sonucu = " + str(sonuc))
    print(" ")

def bol():
    
    sayi1 = int(input("Lütfen 1. Sayıyı Giriniz : "))
    sayi2 = int(input("Lütfen 2. Sayıyı Giriniz : "))

    sonuc = sayi1 / sayi2
    
    print(" ")
    print("Bölme İşleminizin Sonucu = " + str(sonuc))
    print(" ")
    
devam = True


while devam:
    
    print("Lütfen Yapılacak İşlemi Seçiniz : ")
    print("1 - Topla")
    print("2 - Çıkar")
    print("3 - Çarp")
    print("4 - Böl")
    print("5 - Çıkış Yap")
         
    secenek = int(input("Lütfen Yapmak İstediğiniz İşlemin Numarasını Giriniz : "))
     
    
    if secenek == 1:
        topla()
        
    elif secenek == 2:
        cikar()
        
    elif secenek == 3:
        carp()
        
    elif secenek == 4:
        bol()
    
    elif secenek == 5:
        devam = False
        print("Çıkış Yapılıyor")
        
        
        
        
        
        
         