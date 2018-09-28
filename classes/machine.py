class machine:
    def __init__(self,pilha, fita, estados, fim, atual, epson):

        #--- Iniciando atributos
        self.estados = estados #Objeto
        self.fim = fim #lista inteiros
        self.atual = atual #indice
        self.pilha = pilha
        self.fita = fita
        self.epson = epson

    

    def getEstadoAtual(self):
        return self.estados[self.atual]

    def getFim(self):
        return self.estados[self.fim]

'''
    def verificarT(self, c_fitaAtual, c_pilhaAtual):
        retorno, flag = self.getEstadoAtual().isTransicao(c_fitaAtual,c_pilhaAtual, self.getBrancoP())

        if retorno == -1: #Caso Nao achar nenhuma trasição naquele estado
            return -1
        if flag == 0: # achou(E,E,E) só manda avançar a cabeça da FITA
            self.setProxFita()
            self.atual = self.getEstadoAtual().trans[retorno].getNextState() # Mudo para o Proximo Estado
            return 0

        if self.getEstadoAtual().trans[retorno].getTroca() == self.getBrancoP(): #acaso dor Episoln
            print('Estado Atual ANTES POP: %s'%self.getEstadoAtual().getNome())
            print('PILHA ANTES DO POP %s '%self.getPilha())
            self.pop()
            print('PILHA DEPOIS DO POP %s '%self.getPilha())
        else : #Caso nao for Episolon

            print('Estado Atual ANTES PUSH: %s'%self.getEstadoAtual().getNome())
            print('PILHA ANTES DO PUSH %s '%self.getPilha())
            self.push(self.getEstadoAtual().trans[retorno].getTroca())
            print('PILHA DEPOIS DO PUSH %s '%self.getPilha())
        self.atual = self.getEstadoAtual().trans[retorno].getNextState() # Mudo para o Proximo Estado

        self.setProxFita()

        return 1
    '''

class machineManager():
    machines = list()
    MachineAtual = 0

    def addMachine(self, machine):
        self.machines.append(machine)

    def nextMachine(self):
        if(self.MachineAtual +1 < len(self.machines)):
            self.MachineAtual += 1

    def getAtual(self):
        return self.MachineAtual        