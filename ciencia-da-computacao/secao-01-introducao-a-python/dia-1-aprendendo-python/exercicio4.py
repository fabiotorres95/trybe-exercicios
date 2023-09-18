# Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"], o retorno deve ser "Fernanda".

def biggest(user_list):
  result = 0
  index = 0
  while index < len(user_list):
    if len(user_list[index]) > len(user_list[result]):
      result = index
    index += 1
  
  print(user_list[result])

user_input = input("Digite uma lista de nomes separados por espaço: ")
names = user_input.split()
biggest(names)