# Faça um programa que receba um nome e imprima o mesmo na vertical em escada invertida. Exemplo:
# Entrada: PEDRO
# Saída: 
# PEDRO
# PEDR
# PED
# PE
# P

def create_name_stairs(name):
  index = 1
  while index <= len(name):
    print(name)
    index += 1