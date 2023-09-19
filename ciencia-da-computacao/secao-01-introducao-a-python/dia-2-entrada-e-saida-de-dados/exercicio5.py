# Realize esse exercício utilizando TDD: implemente os testes e depois a função 🧪
# Escreva um programa que retorne uma lista com os valores numéricos de 1 a N, mas com as seguintes exceções:
# Números divisíveis por 3 deve aparecer como “Fizz” ao invés do número;
# Números divisíveis por 5 devem aparecer como “Buzz” ao invés do número;
# Números divisíveis por 3 e 5 devem aparecer como “FizzBuzz” ao invés do número.
# Exemplo: 3 -> [1, 2, "Fizz"].

def fizz_buzz(number):
  index = 1
  result = []

  while index <= number:
    if index % 3 == 0 and index % 5 == 0: result.append("FizzBuzz")
    elif index % 3 == 0: result.append("Fizz")
    elif index % 5 == 0: result.append("Buzz")
    else: result.append(index)

    index += 1

  return result