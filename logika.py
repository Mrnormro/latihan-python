#not or and xor

print("=========NOT========")
a = False
c = not a
print("data a =",a)
print("data c =",c)

print("=========OR========") #jika ada true maka true
a = True
b = False
c = a or b
print(a,"OR",b,"=",c)

print("=========AND========") #jika ada false maka false
a = False
b = True
c = a and b
print(a,"AND",b,"=",c)

print("=========XOR========")#jika sama maka false
a = False
b = True
c = a ^ b
print(a,"XOR",b,"=",c)

