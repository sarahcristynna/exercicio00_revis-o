class Pessoa:
#O uso no __init__ serve para atribuir os valores
    def __init__(self, nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura


 #NÃO SE FAZ NECESSARIO O USO DE ASPAS, A NÃO  SER NOS NOMES!
pessoa1 = Pessoa("Sarah", 18, 60, 1.64 )
pessoa2 = Pessoa("Maria", 18, 65, 1.64 )

#self serve para aqualquer objeto, independente da pessoa!
def apresentacao(self):
    print(f"O nome da pessoa consultada é {self.nome}!!! Sua nome idade agora é: {self.idade};")


def fazer_aniversario(self):
    self.idade+=1 #Esse método pega a idade do obejto e soma + 1 
    print(f"Feliz aniversário,{self.nome}!!! Sua nome idade agora é: {self.idade}. ")





#USAR O VARS E MUITO MAIS FACIL, SEM ERROS!
 
print(vars(pessoa1))

#O DICT E MAIS DIFICIL DE LEMBRA,POREM É IGUAL O VARS!
#print(pessoa1.__dict__)

#DESSA MANEIRA MOSTRA SOMENTE O NOME DA PRIMEIRA PESSOA, EXCLUI TODOS OS OUTROS ATRIBUTOS!
#print(f"O nome da 1º pessoa é: {pessoa1.nome}  ")


#for atributo, valor in vars(pessoa2).items():
    #print(atributo+":", valor)


#FORMA DE IDENTIFICAR OS ATRIBUTOS (SEM OS VALORES ) DE UM OBJETO 
  #print(dir(pessoa2))




