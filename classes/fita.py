class fita:
    def __init__(self, conteudo, alfabeto):
        conteudo = list(conteudo)
        self.conteudo = conteudo
        self.alfabeto = list(alfabeto)

    def getElemento(self):
        if len(self.conteudo) != 0:
            return self.conteudo[0]

    def removeElemento(self):
        if len(self.conteudo) != 0:
            self.conteudo.pop(0)

    def getConteudo(self):
        return self.conteudo

    def __str__(self):
        return "Conteudo: %s"%(self.getConteudo())
