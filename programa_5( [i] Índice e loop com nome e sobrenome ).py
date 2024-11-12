nome_sobrenome=input("Nome completo:")
nome_sobrenome=nome_sobrenome.split()
nome=""
#[i]=indice
for i in range(len(nome_sobrenome)):
    nome_sobrenome[i]=nome_sobrenome[i].capitalize()
    if i!=0:
        nome= nome+ " "+nome_sobrenome[i]
    else:
        nome= nome_sobrenome[i]

print(nome)


