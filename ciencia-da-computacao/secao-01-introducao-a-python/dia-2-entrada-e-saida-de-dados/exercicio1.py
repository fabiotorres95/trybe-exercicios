# Faça um programa que receba um nome e imprima o mesmo na vertical em escada invertida. Exemplo:
# Entrada: PEDRO
# Saída: 
# PEDRO
# PEDR
# PED
# PE
# P

def create_name_stairs(name: str):
  letters_list = []
  for letter in name: letters_list.append(letter)

  index = 1
  while index <= len(name):
    result = ''.join(letters_list)
    print(result)
    letters_list.pop()

    index += 1

user_input = input("Digite seu nome: ")
create_name_stairs(user_input)