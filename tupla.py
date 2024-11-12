# Programa para manipular tuplas
minha_tupla = (10, 20, 30, 40, 50)
print(f"A tupla original é: {minha_tupla}")

# Acessando elementos
print(f"O primeiro elemento é: {minha_tupla[0]}")

# Tentando modificar (gerará um erro, pois tuplas são imutáveis)
try:
    minha_tupla[0] = 100
except TypeError as e:
    print(f"Erro: {e}")
