# Faça um programa que, dado um valor n qualquer, tal que n > 1, imprima na tela um quadrado feito de asteriscos de lado de tamanho n. Por exemplo:
# n = 5

# *****
# *****
# *****
# *****
# *****

# Dica: Python sabe multiplicar sequências! Por exemplo, 3 * 'bla' resulta em blablabla. Isso se aplica a listas também, caso você precise.

def squareMaker(n):
  if n <= 1:
    print('erro: o valor deve ser maior que 1')
    return

  index = 1
  while index <= n:
    print('*' * n)
    index += 1

user_input = input('digite um número maior que 1: ')
if not user_input.isnumeric():
  print('erro: não foi digitado um número')
else:
  squareMaker(int(user_input))

  


