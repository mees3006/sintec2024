"""
n1=float(input("nota 1° trimestre:"))
n2=float(input("nota 2° trimestre:"))
n3=float(input("nota 3° trimestre:"))

media=(n1+n2+n3)/3
faltas=float(input("faltas:"))

if media>=6.0 and faltas<250:
    print(f"aprovado com {media:.3} de nota e {faltas} faltas")

elif media<4.0 or faltas>=250:
    print(f"reprovado com {media:.2} de nota e {faltas} faltas")

#(6>media>=4) = (media<6 and media>=4)

else:
    print(f"recuperação com {media:.2} de nota e {faltas} faltas")
"""
   
#par ou impar
import random
cont=int(0)
vit_p=int(0)
vit_ia=int(0)

print(f"regras: o jogos so é ganho com 10 pontos\n\tapenas numeros inteiros\n")

while cont<3:
     num2=(random.randint(1,10))
     print(f"partidas:{cont}")
     print(f"ganhadas:{vit_p}")
     print(f"perdidas:{vit_ia}")
     player=int(input("ações:\n\tPar(1)\n\tImpar(2)\n\tsair(3)\n"))

     if player==3:
        break       
 
     num1=int(input("jogador_1|numero:"))
     print(f"o computador jogou: {num2}\n")

     imp_par=num1+num2

     if player==1:
         if imp_par%2==0:
             print(f"par, jogador ganhou")
             cont=cont+1
             vit_p+=1
         else:
             print("você perdeu")
             cont+=1
             vit_ia+=1

     if player==2:
         if imp_par%2==1:
             print(f"impar, jogador ganhou")
             cont=cont+1
             vit_p+=1
         else:
             print("você perdeu")  
             cont+=1
             vit_ia+=1      

     if vit_p==2:
         print("player ganhou")
         break

     if vit_ia==2:
         print("computador ganhou")  
         break      