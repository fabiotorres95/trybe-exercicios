# Realize esse exercício utilizando TDD: implemente os testes e depois a função 🧪
# Faça uma função que valide um e-mail, lançando uma exceção quando o valor for inválido. Endereços de e-mail válidos devem seguir as seguintes regras:
# Devem seguir o formato nomeusuario@nomewebsite.extensao;
# O nome de usuário deve conter somente letras, dígitos, traços e underscores (_);
# O nome de usuário deve iniciar com uma letra;
# O nome do website deve conter somente letras e dígitos;
# O tamanho máximo da extensão é de 3 caracteres.
# 🦜 As funções isalpha, isdigit e isnumeric podem ser utilizadas para verificar se uma letra ou palavra são compostas de somente caracteres ou dígitos. Exemplo: "1".isalpha() -> False , "a".isalpha() -> True, "123".isnumeric() -> True.

def check_email(email: str):
    
  list1 = email.split('@')
  if len(list1) == 1:
    raise ValueError("Email inválido")
        
      
  list2 = list1[1].split('.')
  if len(list2) == 1:
    raise ValueError("Email inválido")

  username = list1[0]
  website = list2[0]
  extension = list2[1]

  no_underscore = username.replace('_', 'U')
  no_dash = no_underscore.replace('-', 'D')
  if not no_dash.isalnum():
    raise ValueError("Email inválido")
  
  if not username[0].isalpha():
    raise ValueError("Email inválido")
  
  if not website.isalnum():
    raise ValueError("Email inválido")
  
  if len(extension) > 3:
    raise ValueError("Email inválido")
  
  print("Email Válido")
  return True


user_input = input("Digite um email: ")
check_email(user_input)
