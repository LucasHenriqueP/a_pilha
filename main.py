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
    print(est[0].trans[0])
    print(estados)
    inicio = estados.index(inicio)
    fim = estados.index(fim)
    #----------------- Fim do Scraping --------------

    m = machine(pilha1, fita2, est, fim, inicio, epsilon)
    mManager = machineManager()
    mManager.addMachine(m)
    print(mManager.machines[0])

    run(mManager)

def run(mManager):

    machine = mManager.getMachine()

    run = 1
    fimFita = 0
    fimPilha = 0
    fimEstado = 0

    while run:
#---------------- Condições de Parada
        if machine.getFim().getNome() == machine.getEstadoAtual().getNome():
            fimEstado = 1
        if len(machine.getFita().getConteudo()) == 0 :
            fimFita = 1
        if len(machine.getPilha().getConteudo()) == 0:
            fimPilha = 1

        if fimFita == 1:
            if fimEstado == 1 or fimPilha == 1 :
                run = 0
#---------------- Fim das Condições de Parada

        transRetorno = machine.verificarT(machine.getFita().getElemento(),machine.getPilha().getElemento())
        print('Retorno '%transRetorno)

    '''while ( (machine.getPosFita() != machine.getBrancoF()) and ((machine.getEstadoAtual().getNome() != machine.getFim().getNome()) or (machine.isPilhaVazia() == -1) ) ):
        print('-FITA [%s] '%machine.getPosFita())
        print('-Pilha %s '%machine.getPilha())
        print('-Estado Atual: %s'%machine.getEstadoAtual().getNome())
        print('\n')
        existeTrans = machine.verificarT(machine.getPosFita(),machine.getPosPilha())

    print('--FITA [%s] '%machine.getPosFita())
    print('--Pilha %s '%machine.getPilha())
    print('--Estado Atual: %s'%machine.getEstadoAtual().getNome())

    if machine.getEstadoAtual().getNome() == machine.getFim().getNome() and (machine.getPosFita() == machine.getBrancoF()):
        print(bcolors.OKGREEN+'\nACHOU ESTADO FINAL [%s]'%machine.getEstadoAtual().getNome()+bcolors.ENDC)
        exit(1)

    print('\n\n--aab : %d '%machine.isPilhaVazia())
    print('--TOPO PILHA : %s '%machine.getPosPilha())
    print('--PILHA INTEIRA: %s '%machine.getPilha())
    print('--PILHA TAM: %d '%machine.pos_pilha)

    if(((machine.getPosFita() == machine.getBrancoF()) and machine.isPilhaVazia() == -1)):
        print(bcolors.OKGREEN+'\nCHEGOU AO FIM DA FITA'+bcolors.ENDC)
        exit(1)

    elif machine.isPilhaVazia() == 1:
        print(bcolors.FAIL+'\nNÃO ACHOU TRANSAÇÃO'+bcolors.ENDC)
        exit(1)

'''

def main():
    setup();

if __name__ == "__main__":
    main()
