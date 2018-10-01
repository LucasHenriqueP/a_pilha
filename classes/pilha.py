class pilha:
    alfabeto = list()
    def __init__(self, *args):
        if(len(args) == 2):
            conteudo = list()
            if type(args[1]) is not list:
                args1 = args[1].split(' ')
                self.alfabeto = args1
            else:
                print("to no args", args[1])
                self.alfabeto += (args[1])
            self.conteudo = list()
            self.conteudo += list(args[0])
        else:
            print("Erro ao criar pilha")


    def insere(self, valor):
        v = list(valor)
        self.conteudo =  v + self.conteudo

    def getElemento(self):
        return self.conteudo[0]

    def removeElemento(self):
        self.conteudo.pop(0)

    def replica(self):
        rep = pilha(self.conteudo, self.alfabeto)
        return rep

    def getConteudo(self):
        return self.conteudo

    def __str__(self):
        return "Conteudo da pilha é %s" % (self.conteudo)
