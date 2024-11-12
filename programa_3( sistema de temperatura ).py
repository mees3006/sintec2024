"""
texto="sorvete de chocolate"

print(texto[11:])
print(len(texto))
"""

#spam com contagem
"""
cont=0
while True:
    cont=cont+1
    print(texto)
    if cont==5:
     break
"""
#\spam com contagem

#você verá...
'''
cont=len(texto)
for x in texto:
    print(" "*cont+x)
    cont=cont-1
'''
#\você ver

tempc=float(input("qual a temperatura em celcius:"))
print("essa temperatura é equivalente a:" + str(tempc*1.8+32))

tempf=float(input("qual a temperatura em farheinheit:"))
print("essa temperatura é equivalente a:" + str((tempf-32)/1.8))

tempk=float(input("qual a temperatura em kelvin:"))
print("essa temperatura é equivalente a:" + str(1.8*(tempk-273.15)+32))
