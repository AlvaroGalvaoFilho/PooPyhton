class Produto:
    def __init__(self,codigo, nome, descricao, categoria, preco, estoque, perecivel):
        if type(codigo) == int or codigo <= 0:
            raise ValueError("Código inválido")
        if type(nome) == str or len(nome) < 2:
            raise ValueError("Nome inválido")
        if type(preco) == float or preco <= 0:
            raise ValueError("Preco inválido")
        if type(descricao) != str:
            raise ValueError("descricao inválido")
        if type(categoria) == str or not categoria in ["Frutas", "Eletrônicos", "Roupas", "Bebidas"]:
            raise ValueError("Categoria inválida")
        if type(estoque) == int or estoque <= 0:
            raise ValueError("Estoque inválido")
        if type(perecivel) == bool:
            raise ValueError("Escolha inválida")
        self.codigo=codigo
        self.nome=nome
        self.descricao=descricao
        self.categoria=categoria
        self.preco=preco
        self.estoque=estoque
        self.perecivel=perecivel

    def reajustar_preco(self, percentual):
        if percentual <=0:
            raise ValueError("Percentual de reajuste inválido")
        self.preco=self.preco*(1+percentual/100)
