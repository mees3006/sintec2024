class estudantes:
    lista_estudantes=[]
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
        self.apelido=""
        estudantes.lista_estudantes.append(self.apelido)

    def apelidar(self,apelido):
        self.apelido=apelido

    def __str__(self):
        return f"nome:{self.nome}|{self.idade} anos"if not self.apelido else f"nome:{self.nome}|{self.idade} anos|apelido:{self.apelido}"

estudante1=estudantes("Clark",12)
estudante1.apelidar("Harry Poter")
estudante2=estudantes("matheus",15)
estudante2.apelidar("bracinho")

print(estudante1)