class machine:
    def __init__(self,pilha, fita, estados, fim, atual, epson):

        #--- Iniciando atributos
        self.estados = estados #Objeto
        self.fim = fim #lista inteiros
        self.atual = atual #indice
        self.pilha = pilha
        self.fita = fita
        self.epson = epson


    def __str__(self):
        return "Estado Atual: %s"%(self.getEstadoAtual())

    def getEstadoAtual(self):
        return self.estados[self.atual]

    def getFim(self):
        return self.estados[self.fim]

    def getFita(self):
        return self.fita

    def getPilha(self):
        return self.pilha


    def verificarT(self, c_fitaAtual, c_pilhaAtual, mManager):
#------------- Irá Verificar se existe Transição no Estado Atual
        retorno = self.getEstadoAtual().isTransicao(c_fitaAtual,c_pilhaAtual, self.epson, mManager)

#------------- Retorno
        if retorno == -1: #Se Não existir
            return -1 # irá retornar 0
        return 1 # se Existir Irá Retornar 1


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

    def getMachine(self):
        return self.machines[self.MachineAtual]

    def removeMachine(self):
        self.machines.pop(0)

    def __str__(self):
        return "\n ---Manager -> Maquina Atual [%d]"%(self.getAtual())
