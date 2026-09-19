class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3, nota4, nota5):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.nota5 = nota5



    def calcular_media(self):
        soma = self.nota1 + self.nota2 + nota3 + self.nota4 + self.nota5
        self.media = soma/5

        return self.media

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7.0:
            print("Aprovado")
        else:
            print("Reprovado")

aluno1 = Aluno("2026107110930010", "Sarah", 6.3,7.5,10,5.4,9.5)
aluno2 = Aluno("202610711030100", "Maria",5.2,9.5,7.4,3.4,6.9,)
            
           aluno1.calcular_media()
           aluno1.verificao_aprovacao()




#print(vars(aluno1))
#print(vars(aluno2))



