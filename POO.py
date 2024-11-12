def main():
    produto1= produtos("macarrão",11.99,25)
    produto2= produtos("vassoura",14.99,10)
    produto3= produtos("papel higienico",9.99,20)
    produto1.mostrar_info()
    produto1.valor_do_estoque()
    produto2.mostrar_info()
    produto2.valor_do_estoque()

class produtos:
    def __init__(self,nome_do_produto,preço,quantidade):
        self.nome=nome_do_produto
        self.preço=preço
        self.quantidade=quantidade
    def mostrar_info(self):
        print(f"{self.nome}| R${round(self.preço,2)}| {self.quantidade} und")
    def valor_do_estoque(self):
        valor=self.preço * self.quantidade
        print(f"{20*"-"}\nvalor do estoque de {self.nome}:R${round(valor,2)}\n{20*"-"}")

if __name__=="__main__":
    main()