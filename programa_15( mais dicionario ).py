print(f"Bem vindo a lanchonete do joão Zinho!!\n{30*"-"}")
pergunta=input("deseja fazer um pedido? [sim|não]: ").strip().lower()
print(30*"-")
total=0
while pergunta=="sim":
    confraternização={
        1:{"comida":"coxinha",
            "valor":100.50},
        2:{"comida":'beijinho',
        "valor":50.25},
        3:{"comida":"bolinha de queijo",
        "valor":20.00},
        4:{"comida":"pastel de vento",
        "valor":30.50}       
                    }

    for chave,valor in confraternização.items():
        print(f"{chave} - {valor["comida"]}{10*"_"}R${valor["valor"]}")

    nota_fiscal=int(input("pedido: "))

    if nota_fiscal not in confraternização:
        print((f"\n\teste pedido é invalido, tente novamente:\n").capitalize())
    else:
        print(30*"-")
        total+=(confraternização[nota_fiscal]["valor"])
        pergunta=input("quer fazer outro pedido?")

print(f"o valor total de sua compra é: R${total}")    