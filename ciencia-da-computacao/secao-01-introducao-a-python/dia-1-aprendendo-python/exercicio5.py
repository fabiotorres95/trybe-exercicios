# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede (em m²).

import math

def how_much_ink(wall_size: int):
  liters = wall_size / 3
  ink_can = math.ceil(liters / 18)
  price = ink_can * 80

  if ink_can > 1:
    print(f"compre {ink_can} latas de tinta. O custo será de {price},00 R$.")
  else:
    print(f"compre {ink_can} lata de tinta. O custo será de {price},00 R$.")
  
  return (ink_can, price)

user_input = input('Quantos metros quadrados de parede? ')
if not user_input.isnumeric() or int(user_input) <= 0:
  print('digite um valor válido')
else:
  how_much_ink(int(user_input))
  