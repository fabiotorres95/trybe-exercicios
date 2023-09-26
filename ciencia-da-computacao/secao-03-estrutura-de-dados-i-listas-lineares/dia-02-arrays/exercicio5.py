# Em um software gerenciador de servidores, precisamos verificar o número de
# servidores que se comunicam. Os servidores estão representados como um array
# bidimensional onde o valor 1 representa um computador e 0 a ausência do
# mesmo. Dois servidores se comunicam se eles estão na mesma linha ou mesma
# coluna.

# servidores =  [[1,0],[0,1]]
# resultado: 0
# Linhas e colunas são diferentes.

# servidores = [[1,0],[1,1]]
# resultado: 3
# Todos os servidores se comunicam com ao menos um outro servidor.

# servidores = [[1, 0, 0],
#               [1, 0, 0],
#               [0, 0, 1]]
# resultado: 2
# O servidor de índice (2, 2) não possui nenhum outro na mesma linha e coluna.

def server_manager(matrix):
    line = 0
    servers_on = []
    while line < len(matrix):
        column = 0
        while column < len(matrix[line]):
            if matrix[line][column] == 1:
                servers_on.append((line, column))
            column += 1
        line += 1

    connections = 0
    index = 0
    while index < len(servers_on):
        for i in range(len(servers_on)):
            if not i == index:
                if servers_on[index][0] == servers_on[i][0]:
                    connections += 1
                    break
                elif servers_on[index][1] == servers_on[i][1]:
                    connections += 1
                    break
        index += 1

    return connections
