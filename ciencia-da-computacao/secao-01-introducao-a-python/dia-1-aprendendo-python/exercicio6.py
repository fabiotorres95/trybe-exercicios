# Crie uma função que receba os três lado de um triângulo e informe qual o tipo de triângulo formado ou "não é triangulo", caso não seja possível formar um triângulo.

# Dica: Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
  # Triângulo Equilátero: três lados iguais;
  # Triângulo Isósceles: quaisquer dois lados iguais;
  # Triângulo Escaleno: três lados diferentes.

def is_triangle(a, b, c):
  if a + b > c and b + c > a and a + c > b:
    return True
  else:
    return False

def type_of_triangle(a: int, b: int, c: int):
  if is_triangle(a, b, c):
    if a == b == c:
      print("Triângulo Equilátero")
    elif a == b or b == c or a == c:
      print("Triângulo Isósceles")
    else:
      print("Triângulo Escaleno")
  else:
    print("Não é um triângulo.")

input_1 = input("Digite o primeiro lado: ")
input_2 = input("Digite o segundo lado: ")
input_3 = input("Digite o terceiro lado: ")

if input_1.isnumeric and input_2.isnumeric and input_3.isnumeric:
  type_of_triangle(int(input_1), int(input_2), int(input_3))
else:
  print('um ou mais valores não são números inteiros')
