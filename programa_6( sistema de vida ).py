#number=(5,3,4,3)
#for i in number:
 # print(i)

10!=1
#[!] = diferente

#pi=3.141592635
#print(f"o valor aproximado de pi é: {pi:.2f}")

"""
nome=input("nome:")
idade=input("idade:")
cidade=input("cidade:")
apelido=input("apelido:")
if apelido=="homem aranha":
   print(f'{nome} tem {idade} anos e mora em {cidade} e é conhecido como \"{apelido}\" porque seu tio morreu')
else:
   print(f"\t{nome} tem {idade} anos e mora em {cidade}. \n {nome} é conhecido como\"{apelido}\"")
   #\n = new line (nova linha)
   #\t = tabulação(da um respiro\espaços antes do texto)
   #\b = backspace (retira uma letra\simbulo\numero\etc)
"""
import random

vida=40
vida_p=20
energia=0
dano_inimigo=(random.randint(5,15))
score=0

while vida_p>0:
  print(f"\tvida do inimigo:{vida}")
  print(f"\tsua vida:{vida_p}")
  print(f"\tenergia:{energia}")
  print("\tAções:\n\tSoco(+15 energia)\n\tPoção(-15)\n\tMagia(-25 energia)\n\tUlt(-40 energia)\n\tSair")
  ação=input("Ação:").lower().strip

  if ação=="soco":
     vida=vida-(random.randint(1,15))
     energia=energia+15
     vida_p=(vida_p-dano_inimigo)

  if ação=="poçao" and energia>=15:
       vida_p=vida_p+(random.randint(8,15))
       energia=energia-15
  if ação=="poçao" and energia<15:
     print("Você não tem energia suficiente")  

  if ação=="magia" and energia<25:
     print("Você não tem energia suficiente")   
  if ação=="magia" and energia>=25:
     vida=vida-(random.randint(8,15))
     energia=energia-15
     vida_p=vida_p-dano_inimigo

  if ação=="ult" and energia<40:
     print("Você não tem energia suficiente")     
  if ação=="ult" and energia>=40:
     vida=vida-(random.randint(20,30))
     energia=energia-30
     vida_p=vida_p-dano_inimigo

  if ação=="sair":
     print(score)
     break   
     
  if vida_p<=0:
   print("Você morreu") 
   print(f"score:{score}")
   
  if vida<=0:
    score=score+100
    print("\tfelipinho rei delas te matou! seu noob\n\tscore(+100)\n")
    vida=(random.randint(40,100))
    vida_p=vida_p+5

  if vida>=85:
    print("\t!!BOSS!!")    

      
"""
nota_1=int(input("Qual sua nota em 1 tri?:"))
nota_2=int(input("Qual sua nota em 2 tri?:"))
nota_3=int(input("Qual sua nota em 3 tri?:"))
faltas=int(input("Quantas faltas teve?:"))
media=(nota_1+nota_2+nota_3)/3


if (nota_1 and nota_2 and nota_3)>=60 and faltas<250:
    print("aprovado!!")
else:
    print("reprovado")
    

#segundo metodo


#if media>60 and faltas<250:
 #   print("aprovado")
#else:
 #   print("vai estudar")
"""
