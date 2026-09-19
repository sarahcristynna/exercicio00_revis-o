class Livro:
    def __init__(self, titulo,autor,ano,):
        self.titulo = titulo 
        self.autor = autor 
        self.ano = ano

    def editar_titulo(self, novo_titulo):
        self.titulo = novo_titulo

    def mostrar_tudo(self):
    
        print(f"O titulo do livro é: {livro1.titulo}\nO autor é: {livro1.autor},\nO ano de lançamento foi: {livro1.ano}  ")

#\n para quebrar a linha 

livro1 = Livro("Dom Camuro", "Macho de Assis", 1899)
#print(f"O titulo do livro é: {livro1.titulo} ")

livro1.mostrar_tudo()
print("__________________________________________________________")
livro1.editar_titulo("Dom Casmurro")
livro1.mostrar_tudo()

