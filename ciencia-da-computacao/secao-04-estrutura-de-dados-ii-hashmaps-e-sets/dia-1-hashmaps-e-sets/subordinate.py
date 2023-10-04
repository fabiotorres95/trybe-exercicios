# Uma certa empresa tem uma estrutura hierarquizada onde cada pessoa reporta a
# uma única outra pessoa. Cada pessoa tem um score que é o total de pessoas
# que estão abaixo dela, incluindo subordinados de seus subordinados, além
# dela própria. Isso significa que uma pessoa que não tem nenhuma equipe tem
# score 1. Uma pessoa com apenas um subordinado e esse subordinado não tem
# equipe, tem score 2.

# Escreva um método que calcule o score de uma determinada pessoa.

# 👀 De olho na dica: para saber o score de uma pessoa, você precisa saber o
# score das pessoas da equipe dela, correto? Qual estratégia utiliza a mesma
# função dentro dela própria?
