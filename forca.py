# ---------------variaveis----------------------# 
palavra_secreta = "feioso".upper().replace(" ", " ")
palavra_escondida = "_" * len(palavra_secreta)
tentativas=7
letras_erradas=[]
letras_corretas=[]

# ---------------loop|descrição-------------#
while tentativas>0:
    print(f"letras erradas{letras_erradas}")
    print(f"A palavra tem {len(palavra_secreta)} letras.")
    print("Palavra atual:", palavra_escondida.replace("_", "_"))
    print(f"tentativas:{tentativas}")
    print("escreva '1' para sair do jogo")
    letra = input("Escreva uma letra: ").upper()

# -------------ao precionar "1":sair da forca----------------------------------#
    if letra=="1":
        break

# ------------------caso duas letras juntas-----------------#
    if not letra or len(letra) != 1: 
        print("Por favor, digite apenas uma letra.")
        continue

# -------------------------caso letra ja escolhida anteriormente-----------------#
    if (letra in letras_erradas) or (letra in letras_corretas):
        print(20*"-")
        print("esta letra ja foi escrita")
        print(20*"-")
        continue

# -------------------------faz as palavras conseguirem aparecer quando corretas-----------------#
    palavra_escondida = list(palavra_escondida)
    indexacao = 0

# ------------------------adiciona letras erradas numa lista------------------------#
    if letra not in palavra_secreta:
        letras_erradas.append(letra)
        tentativas-=1
# ---------------------------adiciona letras certas numa lista-----------------------#
    else:
        letras_corretas.append(letra)

# -----------------------------mostar a letra certa na forca-------------------------#
    for letra_secreta in palavra_secreta:
        if letra_secreta == letra:
            palavra_escondida[indexacao] = letra
        indexacao += 1
        letras_corretas.append(letra)

    palavra_escondida = "".join(palavra_escondida)
    
# -----------------------------termina o jogo quando a palavra estiver completa--------------#
    if palavra_escondida == "SECRETA_PALAVRA":
        print("Você terminou a palavra:", palavra_escondida)
        break
input()