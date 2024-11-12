loja={
    1:{"jogo":"Red Dead Redemption",
        "valor":1590,
        "genero":"aventura",
        "estoque":7},
     2:{"jogo":"Wath Dogs:Legion",
         "valor":50,
         "genero":"ação",
        "estoque":2},
     3:{"jogo":"Assissini's Creed 2",
         "valor":40,
         "genero":"stealht",
        "estoque":9},
     4:{"jogo":"Batman:Arkhan City",
         "valor":90,
         "genero":"aventura",
        "estoque":12},
         }

total=0

print('''
▀▀█▀▀ █▀▀█ █▀▀▄ █  █ 　  █▀▀█ █▀▀█ █▀▄▀█ █▀▀ █▀▀ 
  █   █  █ █  █ █▄▄█ 　  █ ▄▄ █▄▄█ █ ▀ █ █▀▀ ▀▀█ 
  █   ▀▀▀▀ ▀  ▀ ▄▄▄█ 　  █▄▄█ ▀  ▀ ▀   ▀ ▀▀▀ ▀▀▀''')

pergunta=input("voce quer ver alguns jogos?(sim|não):")

while True:

    while pergunta=="sim":

        for chave,valor in loja.items():
            print(f"{chave} - {valor["jogo"]}")

        p1=int(input("digite o codigo do jogo "))

        if p1 not in loja:
            print("este jogo não esta na lista")
            pergunta=input("voce quer ver outro jogos?:")
        else:
            print(f"o valor de  {loja[p1]["jogo"]} é R${loja[p1]["valor"]}")
            compra=input("você quer comprar este jogo?(sim|não)")
            if compra == "sim":
                (loja[p1]["estoque"])-=1
                total+=loja[p1]["valor"]
                pergunta=input("voce quer ver algum outro jogo?(sim|não):")
            else:
                pergunta=input("voce quer ver algum outro jogo?(sim|não):")

        
    while pergunta=="estoque":
        for chave,valor in loja.items():
            print(f"{chave} - {valor["jogo"]}\nestoque:{valor["estoque"]}|gênero:{valor["genero"]}")
        mudança=input("quer trocar algo?")
        if mudança=="adicionar":
            jogo_add=input("qual jogo vai adicionar?(escreva o nome)")
            valor_add=int(input("qual o valor desse jogo?"))
            quant_add=int(input("quantos vai ter?"))
            gen_add=input("qual o gênero?")
            loja[chave+1]={
                "jogo":jogo_add,
                "valor":valor_add,
                "estoque":quant_add,
                "genero":gen_add,
            }
            pergunta=input("voce quer ver alguns jogos?(sim|não):")

        elif mudança=="remover":
            jogo_remove=int(input("qual jogo vai remover?(escreva o codigo do jogo)"))
            loja.pop(jogo_remove)
            pergunta=input("voce quer ver alguns jogos?(sim|não):")

        else:
            pergunta=input("voce quer ver alguns jogos?(sim|não):")

    if pergunta=="não":
        print(f"o total da sua compra foi: R${total}")
        break



    