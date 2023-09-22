class Tv:
    def __init__(self, tamanho) -> None:
        self.__volume = 50
        self.__canal = 1
        self.__tamanho = tamanho
        self.__ligada = False

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def aumentar_volume(self) -> None:
        if self.__volume < 99:
            self.__volume += 1

    def diminuir_volume(self) -> None:
        if self.__volume > 0:
            self.__volume -= 1

    def modificar_canal(self, canal_input) -> None:
        if type(canal_input) is int and 1 <= canal_input <= 99:
            self.__canal = canal_input
        else:
            raise ValueError('Canal inválido')

    def ligar_desligar(self) -> None:
        self.__ligada = not self.__ligada
