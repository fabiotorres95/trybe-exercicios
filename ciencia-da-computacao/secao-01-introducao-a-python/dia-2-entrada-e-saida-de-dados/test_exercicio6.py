# Realize esse exercício utilizando TDD: implemente os testes e depois a função 🧪
# Faça uma função que valide um e-mail, lançando uma exceção quando o valor for inválido. Endereços de e-mail válidos devem seguir as seguintes regras:
# Devem seguir o formato nomeusuario@nomewebsite.extensao;
# O nome de usuário deve conter somente letras, dígitos, traços e underscores (_);
# O nome de usuário deve iniciar com uma letra;
# O nome do website deve conter somente letras e dígitos;
# O tamanho máximo da extensão é de 3 caracteres.
# 🦜 As funções isalpha, isdigit e isnumeric podem ser utilizadas para verificar se uma letra ou palavra são compostas de somente caracteres ou dígitos. Exemplo: "1".isalpha() -> False , "a".isalpha() -> True, "123".isnumeric() -> True.
import pytest
from exercicio6 import check_email

def test_if_email_contains_at_and_dot():
  with pytest.raises(ValueError, match="Email inválido"):
    check_email('bobsiteorg')

def test_if_username_contains_bad_characters():
  with pytest.raises(ValueError, match="Email inválido"):
    check_email('b;o:b@site.org')
    check_email('b.ob@site.org')
    check_email('b,ob,@site.org')

def test_if_username_starts_with_letter():
  with pytest.raises(ValueError, match="Email inválido"):
    check_email('8ob@site.org')
    check_email('_ob@site.org')
    check_email('-ob@site.org')

def test_if_website_contais_only_letters_and_numbers():
  with pytest.raises(ValueError, match="Email inválido"):
    check_email('bob@s;i:t-e.org')
    check_email('bob@s_ite.org')
    check_email('bob@s#%t&e.org')

def test_if_extension_length_is_3_or_less():
  with pytest.raises(ValueError, match="Email inválido"):
    check_email('bob@site.organization')
    check_email('bob@site.brazil')
    check_email('bob@site.1234')

def test_if_good_email_is_good():
  assert check_email('bob@site.org')
