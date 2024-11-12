import random

cont=0
while cont<10:
    dificuldade=input("dificuldade:\n\tfácil\n\tmédio\n\tdifícil\n")

    if dificuldade=="facil":
         num1=int(input("adivinhe o numero|entre 1 a 5:"))
         Ia=random.randint(1,5)
         if num1==Ia:
            print(f"você acertou!! o numero que o computador escolheu foi {Ia}")
            cont=cont+1
         else:print(f"você errou!! o numero que o computador escolheu foi {Ia}")

    if dificuldade=="medio":
        num1=int(input("adivinhe o numero|entre 1 a 10:"))
        Ia=random.randint(1,10)
        if num1==Ia:
            print(f"você acertou!! o numero que o computador escolheu foi {Ia}")
            cont=cont+1
        else:print(f"você errou!! o numero que o computador escolheu foi {Ia}")

    if dificuldade=="dificil":
        num1=int(input("adivinhe o numero|entre 1 a 20:"))
        Ia=random.randint(1,20)
        if num1==Ia:
             print(f"você acertou!! o numero que o computador escolheu foi {Ia}")
             cont=cont+1
        else:print(f"você errou!! o numero que o computador escolheu foi {Ia}")

