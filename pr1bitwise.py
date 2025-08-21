#----0+++++5----8++++11---

###lebih besar dari 0 lebih kecil dari 5, lebih besar dari 8 lebih kecil dari 11

inputuser = float(input("angka = "))
lebihdari0 = inputuser > 0
#print(lebihdari0)

kurangdari5 = inputuser < 5
#print(kurangdari5)

lebihdari8 = inputuser > 8
#print(lebihdari8)

kurangdari11 = inputuser < 11
#print(kurangdari11)

hasil = lebihdari0 and kurangdari5 or lebihdari8 and kurangdari11
print(hasil)