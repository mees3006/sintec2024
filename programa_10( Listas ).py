"""
num=[2,4,6,8]
senha=int(input("digite um numero:"))

if senha in num:
    print("este numero esta na lista")
else:
    print("este numero não esta na lista")
"""

"""
num=[2,4,6,8]
print(num)

num[3]=10   #adiciona um valor a casa 3 da lista
print(num)

num[2]+=8   #faz operaçoes matematica(+,-,*,/,**) com numero da casa x(neste caso 2) com o numero escolhido 
print(num)

num.append(3)
print(num)

nomes=["andre","bruna","sara"]
print(nomes)
nomes.append((input("insira nome:")).strip())
if 'invalido' in nomes:
    print("este nome é invalido")
    print(nomes)
else:
    print(nomes)

nomes[0]=(input(f"trocar nome {nomes[0]} para:"))
print(nomes)

nomes=sorted(nomes,reverse=True)
print(f"\n{nomes}")
"""


#jeito mais facil
"""
nomes=[]
idades=[]

n1=input("nome:")
n2=input("nome:")
n3=input("nome:")
n4=input("nome:")
n5=input("nome:")

nomes=[n1,n2,n3,n4,n5]
nomes=sorted(nomes)
print(nomes)

i1=int(input("idade:"))
i2=int(input("idade:"))
i3=int(input("idade:"))
i4=int(input("idade:"))
i5=int(input("idade:"))

idades=[i1,i2,i3,i4,i5]
idades=sorted(idades, reverse=True)
print(idades)
"""
#jeito mais complexo
"""
nomes=[]
idades=[]

nomes.append(input("nome:"))
nomes.append(input("nome:"))
nomes.append(input("nome:"))
nomes.append(input("nome:"))
nomes.append(input("nome:"))

nomes=sorted(nomes)
print(nomes)

idades.append(input("idade:"))
idades.append(input("idade:"))
idades.append(input("idade:"))
idades.append(input("idade:"))
idades.append(input("idade:"))

idades=sorted(idades, reverse=True)
print(idades)
"""
#jeito dificil
nomes=[]
for i in range(5):
    nomes.append(input("nome:").strip().capitalize())

idade=[]
for i in range(5):
    idade.append(int(input("numero:")))

nomes=sorted(nomes)
idade=sorted(idade,reverse=True)
print(f"{nomes}\n\t{idade}")


