
import cv2
import os
import time
import numpy as np
import random


def resimDondurme(konum,adet):          #belirtilen konumdaki ilk adet kadar fotoğrafı döndürür ve kaydeder
    sayac = 0
    os.chdir(konum)                     # konuma git
    for i in os.listdir():
        if i.endswith(".jpg") or i.endswith(".png"):
            if sayac < adet:                #adet kadar yapması için

                img = cv2.imread(i)
                img1 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)         #90 derece çevir ve kaydet
                cv2.imwrite(i[:-3]+"d90.jpg",img1)

                img1 = cv2.rotate(img1 ,cv2.ROTATE_90_CLOCKWISE)
                cv2.imwrite(i[:-3]+"d180.jpg", img1)

                img1 = cv2.rotate(img1, cv2.ROTATE_90_CLOCKWISE)
                cv2.imwrite(i[:-3]+"d270.jpg", img1)
                # 3 ker eçevrilip kaydedildi
                sayac += 1

def resimParlaklıkArtırma(konum,adet,brightness):           # belirtilen brightness değeri kadar alındı
    sayac = 0
    os.chdir(konum)
    for i in os.listdir():
        if sayac < adet:
            contrast = 30
            img = cv2.imread(i)
            img = np.int16(img)
            img = img * (contrast / 127 + 1) - contrast - brightness
            img = np.clip(img, 0, 255)
            img = np.uint8(img)
            sayac += 1
            cv2.imwrite(i[:-3] + "b.jpg",img)
            cv2.waitKey(0)


def resimBuyutmeYaDaKucultme(konum,adet,boyut):
    os.chdir(konum)
    uzunluk = len(os.listdir())
    farkli = []
    sayac = 0

    print(uzunluk)
    for i in range(uzunluk):
            print("A")
            if(sayac < adet):
                indis = random.randint(0,uzunluk)
                print("A")
                if indis not in farkli:         #farklı resimler için işlem yapabilmesi için
                    farkli.append(indis)        #bu sayade kontrol ediyorum
                    print("A")
                    isim = os.listdir()[indis]      #istenilen resmin ismine ulaşıldı
                    img = cv2.imread(isim)
                    print("A")
                    img = cv2.resize(img,(int(len(img[0])*boyut),int(len(img)*boyut)))       #tekrar boyutlandırıldı
                    print(isim)
                    print("A")
                    cv2.imwrite(isim[:-3]+"z.jpg",img)                                      #tekrar aynı yere yazıldı
                    sayac += 1
            print("-------------------------")
    print("A")



