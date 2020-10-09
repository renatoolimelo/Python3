
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

    def __str__(self):
        return f'{self._nome} - {self._ano} - {self._likes} Likes'


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    def __str__(self):
        return f'Titulo: {self._nome} - Ano: {self._ano} - Duracao: {self._duracao} - {self._likes} Likes'

    @property
    def duracao(self):
        return self._duracao


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    def __str__(self):
        return f'Titulo: {self._nome} - Ano: {self._ano} - Temporadas: {self._temporadas} - {self._likes} Likes'

    @property
    def temporadas(self):
        return self._temporadas


class Playlist(list):

    def __init__(self, nome, programas):
        self._nome = nome
        super().__init__(programas)

    @property
    def nome(self):
        return self._nome


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
supernatural = Serie("supernatural", 2000, 12)
tmep = Filme("todo mundo em panico", 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
supernatural.dar_like()
supernatural.dar_like()
supernatural.dar_like()
supernatural.dar_like()

filmes_e_series = [vingadores, supernatural, demolidor, tmep]

playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Existe {demolidor in playlist_fim_de_semana}')
