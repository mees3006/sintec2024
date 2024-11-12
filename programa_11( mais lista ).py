"""
animais=["gato","cachocho","pato","cobra"]
print(animais)
    #.remove
animais.remove("cobra")
print(animais)

animais.pop(1)#escolha de elemento da lista(número)
print(animais)

del animais[0]#deleta o elemento de escolha(numero)
print(animais)

animais.clear()
print(animais)


#del animais#deleta a lista inteira
#print(animais)
"""

cores=["azul","vermelho","verde","roxo"]
cores.reverse()
print (cores)

#!!!IMPORTANTE!!!#
for j in range(3):
    for i in range(len(cores)):
        print(i,cores[i])
    print(20*"-")    

f=0
while f<len(cores):
    print(cores[f])
    f+=1

[print(cores[elementos]) for elementos in range(len(cores))]


[print(i) for i in cores]

"""
print(cores)

cores.pop(1)
cores.remove("verde")
print(cores)

cores.insert(0,"rosa")
cores.append("verde")
print(cores)

cores.clear()
print(cores)
"""