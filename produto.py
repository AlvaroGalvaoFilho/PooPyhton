class Produto:
    def __init__(self,codigo, nome, descricao, categoria, preco, estoque, perecivel):
        self.set__codigo(codigo)
        self.set__nome(nome)
        self.set__descricao(descricao)
        self.set__categoria(categoria)
        self.set__preco(preco)
        self.set__estoque(estoque)
        self.set__perecivel(perecivel)

    def reajustar_preco(self, percentual):
        if percentual <=0:
            raise ValueError("Percentual de reajuste inválido")
        self.__preco=self.__preco*(1+percentual/100)


    def set_codigo(self, codigo):
        if type(codigo) != int or codigo <= 0:
            raise ValueError("Código inválido")
        self.__codigo=codigo

    def get_codigo(self):
        return self.__codigo

    def set_nome(self, nome):
        if type(nome) != str or len(nome) < 2:
            raise ValueError("Nome inválido")
        self.__nome=nome
    
    def get_nome(self):
        return self.__nome
    
    def set_descricao(self, descricao):
        if type(descricao) != str:
            raise ValueError("descricao inválido")
        self.__descricao=descricao
    
    def get_descricao(self):
        return self.__descricao
    
    def set_categoria(self, categoria):
        if type(categoria) != str or not categoria in ["Frutas", "Eletrônicos", "Roupas", "Bebidas"]:
            raise ValueError("Categoria inválida")
        self.__categoria=categoria
    
    def get_categoria(self):
        return self.__categoria
    
    def set_preco(self, preco):
        if type(preco) != float or preco <= 0:
            raise ValueError("Preco inválido")
        self.__preco=preco
    
    def get_preco(self):
        return self.__preco
    
    def set_estoque(self, estoque):
        if type(estoque) != int or estoque <= 0:
            raise ValueError("Estoque inválido")
        self.__estoque=estoque
    
    def get_estoque(self):
        return self.__estoque
    
    def set_perecivel(self, perecivel):
        if type(perecivel) != bool:
            raise ValueError("Escolha inválida")
        
    def get_perecivel(self):
        return self.__perecivel