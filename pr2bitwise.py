#++0--5++8--11++

inputuser = float(input("angka = "))
kurangdari0 = inputuser < 0
print(kurangdari0)

lebihdari5 = inputuser > 5
print(lebihdari5)

kurangdari8 = inputuser < 8
print(kurangdari8)

lebihdari11 = inputuser > 11
print(lebihdari11)

hasil = kurangdari0 or lebihdari5 and kurangdari8 or lebihdari11
print(hasil)