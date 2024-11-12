import random
lista_sort=["felipe","bianca","lee","yuri","julia"]
cont=0

print("s lista completa:")
print(lista_sort)
print("nomes sorteados:")

for i in range(len(lista_sort)):
            num_ale=random.randint(0,len(lista_sort)-1)

            nome_rev=lista_sort[num_ale]

            print(f"{i} - {nome_rev}")
            lista_sort.remove(nome_rev)

            input("digite enter para sortear:")



"""
while True:

    perg=input("sortear um nome?:")
    if perg=="sim":
        print(30*"-")

        num_ale=random.randint(0,len(lista_sort)-1)

        nome_rev=lista_sort[num_ale]

        cont+=1
        print(f"{cont} - {nome_rev}")
        lista_sort.remove(nome_rev)

    if lista_sort==[] or perg=="não":
        print(30*"-")
        break
    """