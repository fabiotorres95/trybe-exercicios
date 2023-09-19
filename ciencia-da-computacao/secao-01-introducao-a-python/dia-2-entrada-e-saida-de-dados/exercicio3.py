# Modifique o exercício anterior para que as palavras sejam lidas de um arquivo. Considere que o arquivo terá cada palavra em uma linha.
from exercicio2 import scramble_game

file = open('palavras.txt')
words_list = []

for line in file:
  word = line.strip('\n')
  words_list.append(word)

scramble_game(words_list)