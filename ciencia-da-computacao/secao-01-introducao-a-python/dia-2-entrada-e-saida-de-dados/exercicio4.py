# Dado o seguinte arquivo no formato JSON, leia seu conteúdo e calcule a porcentagem de livros em cada categoria em relação ao número total de livros. O resultado deve ser escrito em um arquivo no formato CSV como o exemplo abaixo.
# Saída:
# categoria,porcentagem
# Python,0.23201856148491878
# Java,0.23201856148491878
# PHP,0.23201856148491878

import json
import csv

try:
  categories_list = []
  with open('books.json') as file:
    json_list = json.load(file)
    for book in json_list:
      categories_list.append(book['categories'])

  count_categories = {}
  for list in categories_list:
    for category in list:
      if not category in count_categories: count_categories[category] = 1
      else: count_categories[category] += 1

  for category in count_categories:
    count_categories[category] = (count_categories[category] / len(categories_list)) * 100


  with open('books.csv', 'w', encoding='utf8') as newFile:
    writer = csv.writer(newFile)

    headers = ["categoria", "porcentagem"]
    writer.writerow(headers)

    for category in count_categories:
      row = [category, count_categories[category]]
      writer.writerow(row)

except FileNotFoundError:
  print('arquivo books.json e/ou books.csv não encontrado')