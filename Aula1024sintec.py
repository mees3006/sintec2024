import os

jogos = [{"nome":"LOL DELUXE", "genero":"MOBA","preco":40.99,"estoque":7},
{"nome":"RDR 4", "genero":"Aventura","preco":579.98, "estoque":8},
{"nome":"Minecraft 2", "genero":"Triangulo","preco":199.99, "estoque":6},
{"nome":"Free Fire","genero":"Battle Royale","preco":0.30,"estoque":50}
]

def main():
    '''exibe o titulo, opções e a pergunta de escolha'''
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()

def exibir_titulo(titulo=""):
    '''imprime o titulo na tela'''
    os.system("cls")
    print('''
████████████████████████████████████████████████████▀███████████████████████████
█▄─▄▄▀█▄─▄█─▄▄▄─██▀▄─██▄─▄▄▀█▄─▄▄▀██▀▄─██─▄▄─███─▄▄▄▄██▀▄─██▄─▀█▀─▄█▄─▄▄─█─▄▄▄▄█
██─▄─▄██─██─███▀██─▀─███─▄─▄██─██─██─▀─██─██─███─██▄─██─▀─███─█▄█─███─▄█▀█▄▄▄▄─█
▀▄▄▀▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀''')
    if titulo != "":
        print(f"\n{titulo}\n")

def exibir_opcoes():
    '''exibe as opções da loja
        ex: mostar jogos'''
    print('''
1. Mostrar Jogos
2. Alterar Estoque
3. Cadastrar Jogo
4. Vender Jogos
5. Sair
''')
    
def mostrar_jogos():
    '''menu que exibe os jogos cadastrados na loja e suas informações.'''
    exibir_titulo("Lista de jogos:")
    for i, jogo in enumerate(jogos, start=1):
        nome_jogo = jogo["nome"]
        genero = jogo["genero"]
        preco = jogo["preco"]
        estoque = jogo["estoque"]
        print(f"{i}-{nome_jogo.ljust(25)} | {genero.ljust(15)} | R${str(preco).ljust(15)} | {str(estoque).ljust(5)}unid.")

def escolher_opcao():
    '''perguta qual opção o usuario irá escolher'''
    try:
        escolha_usuario = int(input("Escolha uma opção do menu: "))
        if escolha_usuario == 1:
            mostrar_jogos()
            voltar_ao_menu()
        elif escolha_usuario == 2:
            mostrar_jogos()
            alterar_estoque()
            voltar_ao_menu()
        elif escolha_usuario == 3:
            cadastrar_jogo()
            voltar_ao_menu()
        elif escolha_usuario == 4:
            mostrar_jogos()
            vender_jogo()
            voltar_ao_menu()
        elif escolha_usuario == 5:
            exibir_titulo("Você saiu do programa.")
        else:
            print("Opção Inválida")
            voltar_ao_menu()

    except:
        print("Opção Inválida")
        voltar_ao_menu()

def voltar_ao_menu():
    '''pede para apertar enter e, caso respondido, abre o main() assim voltando ao menu
       entrada:enter
       saída:volta ao menu'''
    input("\nAperte Enter para voltar ao menu principal.")
    main()

def cadastrar_jogo():
    '''pede as informações(nome, genero, valor e quantidade) de um jogo que você queira adcionar na loja
        entrada:nome, genero, valor e quantidade
        saída:adiciona o jogo na loja'''
    nome_do_jogo=input("qual o nome do jogo que voce quer cadastrar:")
    genero=input("digite o gênero do jogo:")
    preço=float(input("digite o preço do jogo:"))
    estoque=int(input("digite a quantidade de jogos:"))
    dados_do_jogo={"nome":nome_do_jogo,"genero":genero,"preco":preço,"estoque":estoque}
    jogos.append(dados_do_jogo)

def vender_jogo():
    '''pergunta qual jogo você irá vender, e diminui a quantidade do jogo escolhido'''
    vender=input("qual jogo você vai vender")
    quantidade=int(input("quantos vai vender"))
    jogo_indisponivel=0
    for jogo in jogos:
        if vender == jogo["nome"]:
            jogo_indisponivel=1
            if jogo["estoque"]<quantidade:
                print("quantidade Inválida")
                voltar_ao_menu()
            else:
                jogo["estoque"]-=quantidade
                voltar_ao_menu()
    if jogo_indisponivel==0:
        print("Opção Inválida")
        voltar_ao_menu()

def alterar_estoque():
    '''Pede o jogo que deseja alterar estoque, depois de escolhido, o usúario pode alterer a quantidade de unidades desse jogo
       entrada:nome, valor do estoque
       saída:muda a quantidade de unidades do jogo escolhido'''
    nome_jogo = input("\nQual jogo quer Alterar o Estoque:")
    for jogo in jogos:
        if nome_jogo == jogo["nome"]:
            estoque = input(f"Qual é o novo valor de estoque? (Atual:{jogo["estoque"]})")
            jogo["estoque"] = int(estoque)
            print(f"{nome_jogo} | {jogo["genero"]} | {jogo["preco"]} | {jogo["estoque"]}")
        

#input()


if __name__ == '__main__':
    main()
