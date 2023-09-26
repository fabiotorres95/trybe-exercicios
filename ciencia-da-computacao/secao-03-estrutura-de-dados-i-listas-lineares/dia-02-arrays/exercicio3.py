# Imagine que você esteja trabalhando em um e-commerce, e foi lhe dado a
# demanda de analisar um array de números inteiros que representam os produtos
# dessa empresa. Verifique quantos produtos formam boas combinações, ou seja,
# quando um produto é igual ao outro e seu índice é maior que o anterior. Esta
# combinação pode ser utilizada para modificar os produtos de uma página. Por
# exemplo:

# Exemplo 1:
# produtos = [1, 3, 1, 1, 2, 3]
# resultado = 4
# Os índices (0, 2), (0, 3), (1, 5), (2, 3) formam combinações.

# Exemplo 2:
# produtos = [1, 1, 2, 3]
# resultado = 1
# Os índices (0, 1) formam a única combinação.

def combinations(data):
    index = 0
    result = []
    while index < len(data):
        for i in range(index + 1, len(data)):
            if data[index] == data[i]:
                result.append((index, i))
        index += 1

    string_result = ''
    for i in result:
        if i == result[-1]:
            string_result += f'({i[0]}, {i[1]})'
        else:
            string_result += f'({i[0]}, {i[1]}), '

    print(f'resultado = {len(result)}')
    if len(result) > 1:
        print(f'Os índices {string_result} formam combinações.')
    elif len(result) == 1:
        print(f'Os índices {string_result} formam a única combinação.')
    else:
        print('Não há combinações.')
