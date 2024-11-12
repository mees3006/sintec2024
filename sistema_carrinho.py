print(f"Bem vindo a lanchonete do joão Zinho!!\n{30*"-"}")
pergunta=input("deseja fazer um pedido?: ").strip().lower()
print(30*"-")

carrinho=[]
total=0


while pergunta=="sim" or "carrinho":
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

    if pergunta=="sim":
        for chave,valor in confraternização.items():
            print(f"{chave} - {valor["comida"]}{10*"_"}R${valor["valor"]}")

        nota_fiscal=int(input("pedido: "))

        if nota_fiscal not in confraternização:
            print((f"\n\teste pedido é invalido, tente novamente:\n").capitalize())
        else:
            print(30*"-")
            total+=(confraternização[nota_fiscal]["valor"])
            carrinho.append(confraternização[nota_fiscal])
            pergunta=input("quer fazer outro pedido?")

    if pergunta=="carrinho":
        car_rev=input(f"oque voce quer tirar?\n{carrinho}\n")
        if car_rev in carrinho:
            carrinho.remove(car_rev)
            pergunta=input("deseja fazer um pedido?: ").strip().lower()
        else:
            print("item invalido")
            pergunta=input("deseja fazer um pedido?: ").strip().lower()
        
print(f"o valor total de sua compra é: R${total}")    