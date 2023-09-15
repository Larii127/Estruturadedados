class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'Ola, meu nome é {self.nome}, tenho {self.idade} anos')

pessoa = Pessoa('Amanda', 24)
pessoa.falar()