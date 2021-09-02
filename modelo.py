#controle de playlist de programa de TV.

class Programa: # #herança é herdado pelas classes filme e serie não precisamos replicar as informaçoes em todas as classes. #classe programa é a nossa classe mae
    def __init__(self, nome, ano):  # atributos nome,ano,duracao #construtor __init__ é o inicializador da classe para criar o objeto
        self._nome = nome.title()  # valores do objeto # .title() irá imprimir as primeiras letras de cada palavra em maiúsculo
        self.ano = ano  # valores do objeto
        self._likes = 0  # __ ou _ para proteger o atributo (deixar privado)

    @property  # usamos property para o codigo nao quebrar, retorna o valor que desejamos # se criamos getters e setters todos os lugares que já acessam a classe precisam mudar.
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property  # propety é um encapsulamento
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes' #representa o objeto programa na classe Programa em forma de texto

# qual é o beneficio de usar HERANÇA: consigo utilizar informacoes que estao na classe mae,

class Filme(Programa): #herança  o método abastecer é herdado pelas classes Moto e Carro. entre () esta nosso parametro q é a classe mae
    def __init__(self, nome, ano, duracao): #atributos nome,ano,duracao #construtor __init__
        super().__init__(nome, ano) #com a funcao super estou chamando a classe mae (programa)
        self.duracao = duracao #valores do objeto #este atributo esta publico

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

#f'uma string {variavel}') irá juntar o valor da variável após o texto uma string
#Dentro de {} esta o atributo que queremos imprimir.


class Serie (Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

    def __getitem__(self, item): #representa o comportamento de uma lista
        return self._programas[item]



vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

#print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}')

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

print(playlist_fim_de_semana[0])

for programa in playlist_fim_de_semana.listagem:
    print(programa)