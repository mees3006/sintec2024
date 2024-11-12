
#------------------------------------------------------------------#
#modo construtor
# dicionario_2=dict(nome="ababa",
#                   idade=180,
#                   sexo="nem sabe oque significa")

# print(dicionario_2["nome"])
# print(len(dicionario_2))

#------------------------------------------------------------------#
# mudando dicionario em comando
# dicionario_2["idade"]+=1
# print(dicionario_2["idade"])


#-------------------------------------------------------------------#
#modo simplificado(melhor)
# dicionario={"nome":"Tiago",
#             "idade":19,
#             "sexo":"masculino"}

# print(dicionario["nome"])
# print(len(dicionario))

# print(dicionario.keys())
# print(dicionario.values())
# print(dicionario.items())

# -----------------------------------------------------------------------#
# atividade

# dick={}

# dick["nome"]=input("nome:")
# dick["idade"]=input("idade:")
# dick["sexo"]=input("sexo:")

# print(f"as chaves do dicionario sao:{dick.keys()}")
# print(f"os valores do dicionario sao:{dick.values()}")
# print(f"os conjuntos do dicionario sao:{dick.items()}")

# dick["nome"]="rafa"
# dick.update({"idade":20})
# print(f"os valores do dicionario sao:{dick.values()}")

pergunta=input("voce quer saber a nota de um aluno?(sim|não):")

while pergunta=="sim":
    dick={
        1:{"nome":"felipe",
        "nota":60},
        2:{"nome":"pablito",
        "nota":100},
        3:{"nome":"yuri",
        "nota":90}
    }

    dick[4]={"nome":"cassio",
            "nota":27}

    for chave,valor in dick.items():
        print(f"{chave} - {valor["nome"]}")

    aluno=int(input("digite o RA para saber a nota: "))

    if aluno not in dick:
        print("este aluno não esta na lista")
        pergunta=input("voce quer saber a nota de um aluno?:")
    else:
        print(f"a nota de {dick[aluno]["nome"]} é {dick[aluno]["nota"]}")

        pergunta=input("voce quer saber a nota de mais um aluno?:")
