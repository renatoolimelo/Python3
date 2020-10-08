
class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano

    @property
    def duracao(self):
        return self.__duracao

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano

    @property
    def temporadas(self):
        return self.__temporadas

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
vingadores.nome = "capitã marvel"
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao}'
      f' - Likes: {vingadores.likes}')

supernatural = Serie("supernatural", 2000, 12)
supernatural.dar_like()
supernatural.dar_like()
supernatural.nome = "o alto da compadecida"
print(f'Nome: {supernatural.nome} - Ano: {supernatural.ano} - Temporadas: {supernatural.temporadas}'
      f' - Likes: {supernatural.likes}')


