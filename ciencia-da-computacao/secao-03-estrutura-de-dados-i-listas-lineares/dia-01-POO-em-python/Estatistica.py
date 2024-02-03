from collections import Counter


class Estatistica:
    def __init__(self, numbers) -> None:
        self.__numbers = numbers

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def media(self):
        return sum(self.__numbers) / len(self.__numbers)

    def mediana(self):
        self.__numbers.sort()
        if len(self.__numbers) % 2 == 0:
            metade_maior = self.__numbers[len(self.__numbers) // 2]
            metade_menor = self.__numbers[len(self.__numbers) // 2 - 1]
            return (metade_maior + metade_menor) / 2
        else:
            return self.__numbers[len(self.__numbers) // 2]

    def moda(self):
        counter = Counter(self.__numbers)
        return counter.most_common(1)[0][0]
