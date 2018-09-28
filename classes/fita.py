class fita:
    def __init__(self, conteudo, alfabeto):
        conteudo = list(conteudo)
        self.conteudo = conteudo
        self.alfabeto = list(alfabeto)

    def getElemento(self):
        return self.conteudo[0]

    def removeElemento(self):
        self.conteudo.pop(0)   


