
class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @property
    def ano(self):
        return self._ano

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
vingadores.nome = "capitã marvel"
print(f'{vingadores.nome} - {vingadores.ano} - {vingadores.duracao} : {vingadores.likes}')

supernatural = Serie("supernatural", 2000, 12)
supernatural.dar_like()
supernatural.dar_like()
supernatural.nome = "o alto da compadecida"
print(f'{supernatural.nome} - {supernatural.ano} - {supernatural.temporadas} : {supernatural.likes}')

filmes_e_series = [vingadores, supernatural]

for programa in filmes_e_series:
    detalhes = programa.duracao if (hasattr(programa, 'duracao')) else programa.temporadas
    print(f'{programa.nome} - {programa.ano} - {detalhes} : {programa.likes}')
