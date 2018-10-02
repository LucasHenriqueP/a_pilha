from copy import deepcopy
from classes.machine import *

class Estado:
    def __init__(self, nome):
        self.nome = nome
        self.trans = list()

    def __str__(self):
        return self.getNome()

    def getNome(self):
        return self.nome

    def addTransicao(self, trans):
        self.trans.append(trans)

    def verificaInicialPilha(self, atual, pilha):
        l = []
        for i in atual:
            if i not in l:
                if i != pilha.getBranco():
                    l.append(i)
        atual = l
        return atual

    def isTransicao(self, c_fita, c_pilha, episolon, mManager):

        '''

        E dizia Jesus: Pai, perdoa-lhes, porque não sabem o que fazem.
                                                                        Lucas 23:34

        '''

        retorno = -1 #Acaso nao entrar nas condições abaixo irá retornar -1(Não achou nenhuma transição naquele estado)

        for i in range(len(self.trans)):

            if self.trans[i].getCFita() == episolon:
                if (self.trans[i].getCPilha() == c_pilha):
                    if (self.trans[i].getTroca() == episolon):
                        #E,x,E - NextCabecaFita(), Pop(), NextState()

                        pilha = deepcopy(mManager.getMachine().getPilha())
                        pilha.removeElemento() # Pop()
                        fita = deepcopy(mManager.getMachine().getFita())
                        fita.removeElemento() #NextCabecaFita()
                        inicio = self.trans[i].getNextState() #NextState()

                        m = machine(pilha, fita, mManager.getMachine().estados, mManager.getMachine().fim, inicio, episolon)
                        mManager.addMachine(m)

                        retorno = 1
                    else:
                        #E,X,X - NextCabecaFita(), Push(x), NextState()
                        pilha = deepcopy(mManager.getMachine().getPilha())
                        x = self.verificaInicialPilha(self.trans[i].getTroca(), pilha)
                        pilha.insere(x) # push(x)
                        fita = deepcopy(mManager.getMachine().getFita())
                        fita.removeElemento() #NextCabecaFita()
                        inicio = self.trans[i].getNextState() #NextState()

                        m = machine(pilha, fita, mManager.getMachine().estados, mManager.getMachine().fim, inicio, episolon)
                        mManager.addMachine(m)


                        retorno = 1
            if self.trans[i].getCPilha() == episolon:
                if (self.trans[i].getCFita() == c_fita):
                    if (self.trans[i].getTroca() == episolon):

                        pilha = deepcopy(mManager.getMachine().getPilha())
                        fita = deepcopy(mManager.getMachine().getFita())
                        fita.removeElemento() #NextCabecaFita()
                        inicio = self.trans[i].getNextState() #NextState()

                        m = machine(pilha, fita, mManager.getMachine().estados, mManager.getMachine().fim, inicio, episolon)
                        mManager.addMachine(m)

                        #x,E,E - NextCabecaFita(), NextState()
                        retorno = 1
                    else:
                        #x,E,X - NextCabecaFita(), Push(x), NextState()

                        pilha = deepcopy(mManager.getMachine().getPilha())
                        x = self.verificaInicialPilha(self.trans[i].getTroca(), pilha)
                        pilha.insere(x) # push(x)
                        fita = deepcopy(mManager.getMachine().getFita())
                        fita.removeElemento() #NextCabecaFita()
                        inicio = self.trans[i].getNextState() #NextState()

                        m = machine(pilha, fita, mManager.getMachine().estados, mManager.getMachine().fim, inicio, episolon)
                        mManager.addMachine(m)

                        retorno = 1

            if (self.trans[i].getCFita() == c_fita) and (self.trans[i].getCPilha() == c_pilha):
                    if (self.trans[i].getTroca() == episolon):
                        # x,x,E - NextCabecaFita(), Pop(), NextState()

                        pilha = deepcopy(mManager.getMachine().getPilha())
                        pilha.removeElemento() # Pop()
                        fita = deepcopy(mManager.getMachine().getFita())
                        fita.removeElemento() #NextCabecaFita()
                        inicio = self.trans[i].getNextState() #NextState()

                        m = machine(pilha, fita, mManager.getMachine().estados, mManager.getMachine().fim, inicio, episolon)
                        mManager.addMachine(m)
                        retorno = 1
                    else:
                        #x,x,x - NextCabecaFita(), Push(x), NextState()
                        pilha = deepcopy(mManager.getMachine().getPilha())
                        x = self.verificaInicialPilha(self.trans[i].getTroca(), pilha)
                        pilha.insere(x) # push(x)
                        fita = deepcopy(mManager.getMachine().getFita())
                        fita.removeElemento() #NextCabecaFita()
                        inicio = self.trans[i].getNextState() #NextState()

                        m = machine(pilha, fita, mManager.getMachine().estados, mManager.getMachine().fim, inicio, episolon)
                        mManager.addMachine(m)
                        retorno = 1

            if (self.trans[i].getCFita() == episolon) and (self.trans[i].getCPilha() == episolon):
                    if (self.trans[i].getTroca() == episolon):
                        # E,E,E - NextState()
                        pilha = deepcopy(mManager.getMachine().getPilha())
                        fita = deepcopy(mManager.getMachine().getFita())
                        inicio = self.trans[i].getNextState() #NextState()

                        m = machine(pilha, fita, mManager.getMachine().estados, mManager.getMachine().fim, inicio, episolon)
                        mManager.addMachine(m)
                        retorno = 1
                    else:
                        pilha = deepcopy(mManager.getMachine().getPilha())
                        x = self.verificaInicialPilha(self.trans[i].getTroca(), pilha)
                        pilha.insere(x) # push(x)
                        fita = deepcopy(mManager.getMachine().getFita())
                        inicio = self.trans[i].getNextState() #NextState()


                        m = machine(pilha, fita, mManager.getMachine().estados, mManager.getMachine().fim, inicio, episolon)
                        mManager.addMachine(m)
                        #E,E,x - Push(x),NextState()
                        retorno = 1

        mManager.removeMachine()
        return retorno



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
