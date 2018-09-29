class Estado:
    def __init__(self, nome):
        self.nome = nome
        self.trans = list()

    def getNome(self):
        return self.nome

    def addTransicao(self, trans):
        self.trans.append(trans)

    def isTransicao(self, c_fita, c_pilha, episolon):
        indexes = list()
        for i in range(len(self.trans)):

            if self.trans[i].getCFita() == episolon:
                if (self.trans[i].getCPilha() == c_pilha):
                    indexes.append(i) #Para fazer Nao deterministico Esse I devera ser gravado em uma LISTA

            if self.trans[i].getCPilha() == episolon:
                if (self.trans[i].getCFita() == c_fita):
                    indexes.append(i) #Para fazer Nao deterministico Esse I devera ser gravado em uma LISTA

            if (self.trans[i].getCFita() == c_fita) and (self.trans[i].getCPilha() == c_pilha):
                indexes.append(i) #Para fazer Nao deterministico Esse I devera ser gravado em uma LISTA

            if (self.trans[i].getCFita() == episolon) and (self.trans[i].getCPilha() == episolon):
                if (self.trans[i].getTroca() == episolon):
                    return (i,0)
                indexes.append(i) #Para fazer Nao deterministico Esse I devera ser gravado em uma LISTA



        return indexes



class Transicao:
    def __init__(self, c_fita, c_pilha, troca, nextState):

        self.c_fita = c_fita
        self.c_pilha = c_pilha
        self.troca = troca
        self.nextState = nextState

    def __str__(self):
        return "Conteudo da Fita %s\nConteudo da Pilha %s\nValor a ser Trocado %s\nProximo Estado %s" % (self.c_fita, self.c_pilha, self.troca, self.nextState)

    def getCFita(self):
        return self.c_fita

    def getCPilha(self):
        return self.c_pilha

    def getTroca(self):
        return self.troca

    def getNextState(self):
        return self.nextState
