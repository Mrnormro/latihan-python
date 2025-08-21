inputuser = float(input("masukkan angka yang bernilai angka yang\nlebih kecil dari 3 atau lebih besar dari 10 :"))


#+3-
kurangdari3 = (inputuser < 3)
print(kurangdari3)
#-10+
lebihdari10 = (inputuser > 10)
print (lebihdari10)
#+3-10+
antara = kurangdari3 or lebihdari10
print(antara)

#-3+10-
inputuser = float(input("masukkan angka yang bernilai angka yang\nlebih besar dari 3 atau lebih kecil dari 10 :"))

#-3+
lebihdari3 = (inputuser > 3)
print(lebihdari3)
#+10-
kurangdari10 = (inputuser < 10)
print (kurangdari10)
#-3+10-
antara1 = lebihdari3 and kurangdari10
print(antara1)