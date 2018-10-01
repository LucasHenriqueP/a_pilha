import sys
import string


from copy import deepcopy
from classes.machine import *
from classes.estados import *
from classes.pilha import *
from classes.fita import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def setup():
    #----------------- Começo do Scraping --------------
    arq = sys.argv[1]
    entrada = sys.argv[2]
    entrada = entrada.replace(" ", "")

    f = open(arq, 'r')
    line = f.readline() #Linha 1 - Alfabeto de Entrada Fita
    alfaFita = line.replace('\n', '')
    alfaFita = alfaFita.replace(' ', '')
    fita2 = fita(entrada, alfaFita)

    line = f.readline() #Linha 2 - Alfabeto de Entrada Pilha
    alfaPilha = line.replace('\n', '')


    line = f.readline() #Linha 3 - Simbolo que representa o epsilon
    line = line.replace("\n", '')
    epsilon = line

    line = f.readline() #Linha 4 - Simbolo Inicial da Pilha
    simboloInicial = line.replace("\n", '')

    pilha1 = pilha(simboloInicial, alfaPilha)

    line = f.readline() #Linha 5 - Conjunto de Estados
    line = line.replace("\n", "")
    estados = line.split(" ")
    estados.sort() #Ordena os Estados


    line = f.readline() #Linha 6 - Estado Inicial
    inicio = line.replace("\n", "")

    line = f.readline() #Linha 7 - Estado Final
    fim = line.replace("\n", "")
    #fim = fim.split(" ")
    #fim.sort()

    est = list()
    for i in range(len(estados)):
        est.append(Estado(str(estados[i])))


    for line in f:
        trans = line.replace("\n", '')
        trans = trans.split(" ")
        pos = trans[0]
        nextState = estados.index(trans[3]) #Trabalho com o Indice nao o Nome
        transicao = Transicao(trans[1], trans[2], trans[4], nextState)
        est[estados.index(pos)].addTransicao(transicao)
    #print(est[0].trans[0])
    #print(estados)
    inicio = estados.index(inicio)
    fim = estados.index(fim)
    #----------------- Fim do Scraping --------------

    m = machine(pilha1, fita2, est, fim, inicio, epsilon)
    mManager = machineManager()
    mManager.addMachine(m)
    #print(mManager.machines[0])

    run(mManager)

def run(mManager):

#----- Variaveis para controlar o Fim da Maquina
    fimFita = 0     # 0 não chegou fim da Fita, se 1 Chegou ao fim da Fita
    fimPilha = 0    # 0 não chegou ao fim da Pilha, se 1 Chegou ao Fim da Pilha
    fimEstado = 0   # 0 não chegou ao um Estado Final, 1 Chegou a um Estado Final

    while True:
        machine = mManager.getMachine()
        #--------------- Debug Visual
        print("Config Antes da Maquina Começar")
        print(mManager) #Maquina Atual no manager e Tamanho do Manager
        print(mManager.getMachine()) #Estado Atual da MaquinaAtual no Manager
        print(mManager.getMachine().getFita()) #Fita completa da Maquina Atual no Manager
        print(mManager.getMachine().getPilha()) #Pilha Completa da Maquina Atual no Manager
        print('---------------------------------------------------')

#---------------- Condições de Parada
        if machine.getFim().getNome() == machine.getEstadoAtual().getNome():
            fimEstado = 1
        if len(machine.getFita().getConteudo()) == 0 :
            fimFita = 1
        if len(machine.getPilha().getConteudo()) == 0:
            fimPilha = 1

        if fimFita == 1:
            if fimEstado == 1 or fimPilha == 1 :
                #run = 0
                break
#---------------- Fim das Condições de Parada

#-------------- Verifica se Existe Transição no Estado Atual
        transRetorno = machine.verificarT(machine.getFita().getElemento(),machine.getPilha().getElemento(),mManager)

#--------------- Se não existe trasição:
        print('Retorno [%d] - Tam Machina [%d]'%(transRetorno,len(mManager.machines)))

        if transRetorno == -1:
            if len(mManager.machines) > 0:      #Verifica se o Manager tem mais maquinas
                #mManager.nextMachine()          #se sim Avança
                mManager.removeMachine()          #se sim Avança
            else:
                print(bcolors.FAIL+"Não achou Transição "+bcolors.ENDC)    #se não Aborta
                exit(0)

#--------------- Debug Visual
        print(mManager) #Maquina Atual no manager e Tamanho do Manager
        print(mManager.getMachine()) #Estado Atual da MaquinaAtual no Manager
        print(mManager.getMachine().getFita()) #Fita completa da Maquina Atual no Manager
        print(mManager.getMachine().getPilha()) #Pilha Completa da Maquina Atual no Manager

        input(bcolors.WARNING+'Pressione Qualquer Tecla para avançar!'+bcolors.ENDC)

#--------------- Verificador para saber pelo o que a Maquina Terminou
    if fimPilha == 1:
        print(bcolors.OKGREEN+"Termino por Fim da Fita e Fim da Pilha"+bcolors.ENDC)
    elif fimEstado == 1:
        print(bcolors.OKGREEN+"Termino por Fim da Fita e Fim por Estado"+bcolors.ENDC)

def main():
    setup();

if __name__ == "__main__":
    main()
