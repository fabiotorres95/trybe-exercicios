# Em um software monitor, o qual verifica a resiliência de outro software,
# precisamos saber o tempo máximo que um software permaneceu sem
# instabilidades. Para isto, a cada hora é feito uma requisição ao sistema
# para verificamos se está tudo bem. Supondo um array que contenha os estados
# coletados por nosso software, calcule quanto tempo máximo que o servidor
# permaneceu sem instabilidades.

# Exemplo:
# 1 - OK
# 0 - Instabilidades

# valores_coletados = [0, 1, 1, 1, 0, 0, 1, 1]
# resultado = 3

# valores_coletados = [1, 1, 1, 1, 0, 0, 1, 1]
# resultado = 4

def check_estability(data):
    best = 0
    recent = 0
    for i in data:
        if i == 1:
            recent += 1
            if recent > best:
                best = recent
        else:
            recent = 0

    return best
