class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        print(f"Esse é o titulo do livro:{self.titulo}")
        print(f"Esse é o autor do livro:{self.autor}")

livro1 = Livro("A marca de uma lagrima", "Pedro Bandeira")
livro1.detalhes()



