from Veri_Coklama_Araci.functions.functions import *

def uygunsaKucultyadaBuyut(variables):
    if(variables.location != "" and variables.count != 0 and variables.zoom != 0):
        resimBuyutmeYaDaKucultme(variables.location,variables.count,variables.zoom)


def uygunsaParlaklikDegis(variables):
    if(variables.location != "" and variables.count != 0 and variables.brightness != 0):
        resimParlaklıkArtırma(variables.location,variables.count,variables.brightness)

def uygunsaDondur(variables):
    print("başladı")
    if (variables.location != "" and variables.count != 0):
        print("başladı 2")
        resimDondurme(variables.location, variables.count)
    print("bitti")
