# Jogo da palavra embaralhada. Desenvolva um jogo em que a pessoa usuária tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras e escolherá uma aleatoriamente. O jogador terá três tentativas para adivinhar a palavra. Ao final, a palavra deve ser mostrada na tela, informando se a pessoa ganhou ou perdeu o jogo.

# 🦜 Para embaralhar uma palavra faça: scrambled_word = "".join(random.sample(word, len(word)))

# 🦜 O sorteio de uma palavra aleatória pode ser feito utilizando o método choice: random.choice(["word1", "word2", "word3"]) -> "word2".
import random

words_list = ["ABACAXI", "COMPUTADOR", "LOUCURA", "JABUTICABA", "ESPINGARDA"]
goal = random.choice(words_list)
print(''.join(random.sample(goal, len(goal))))

user_input = ''
tries = 1
while tries <= 3:
  print("")
  print(f"Tentativa {tries}")
  user_input = input("Adivinhe a palavra embaralhada: ").upper()

  if user_input == goal:
    print("VOCÊ ACERTOU! PARABÉNS!")
    break

  print("Palavra errada!")

  tries += 1

print("")
print("FIM DE JOGO")