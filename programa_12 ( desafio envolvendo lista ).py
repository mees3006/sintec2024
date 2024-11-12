nome_p=[]
num_p=int(input("Quantos presentes vai ter neste natal?:"))
for i in range(num_p):
    nome_p.append(input("Qual presente?:").strip().lower())
    print(20*"-")

print(nome_p)


escolha=input("deseja que algo seja removido?:").strip().lower()  
if escolha=="sim":
    remover=(str(input("oque queres apagar?:").strip().lower()))
    if remover not in nome_p:
        print(f"{remover} não esta na lista")
    nome_p.remove(remover)
    for j in range(len(nome_p)):
        print(nome_p[j])    
        print(20*"-") 
        
if escolha=="não":
     for j in range(len(nome_p)):
        print(nome_p[j])    
        print(20*"-")

else:
    print(f"{escolha} não é uma opção")

