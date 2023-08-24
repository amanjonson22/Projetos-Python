from listas import limites
from listas import oleo
from listas import velocidades
from listas import motor
from listas import sop
from listas import trip
from listas import check
from listas import before_takeoff
from listas import execucao
from listas import transferencia
from listas import nav
from listas import beacon
from listas import landing
from listas import strobe


def limites():
    info_lista = 0
    voltar = False
    while not voltar:
        print('\n#Pesos')
        print('#Limites operacionais (LO)')
        print('#Combustível')
        print('#Óleo')
        print('#Velocidades Características (VC)')
        print('#Motor')
        print('#Voltar\n')
        querer = input('Qual informação você quer? ').lower()
        if querer == 'voltar':
            print('\nVoltar')
            voltar = True
            return voltar
        elif querer == 'pesos':
            print('\nPesos\n')
            print('Peso Máximo de Taxi & Rampa - 600 kg\n') 
        elif querer == 'lo':
            print('\nLimites operacionais\n')
            for i in limites:
                print(limites[info_lista])
                info_lista += 1
        elif querer == 'combustível':
            print('\nCombustível')
            print('Combustível utilizável por tanque - 68L\n')
        elif querer == 'óleo':
            print('\nÓleo\n')
            for i in oleo:
                print(oleo[info_lista])
                info_lista += 1
        elif querer == 'vc':
            print('\nVelocidades Características\n')
            for i in velocidades:
                print(velocidades[info_lista])
                info_lista += 1
        elif querer == 'motor':
            print('\nMotor\n')
            for i in motor:
                print(motor[info_lista])
                info_lista += 1
        info_lista = 0

def exterior():
    print('\n#Checklist')
    print('#Flow expandido(expandido)')
    print('\n#Voltar')

def bs():
    print('\n#Checklist')
    print('#Flow expandido(expandido)')
    print('\n#Voltar')

def es():
    print('\n#Checklist')
    print('#Flow expandido(expandido)')
    print('\n#Voltar')

def a_s():
    print('\n#Checklist')
    print('#Flow expandido(expandido)')
    print('\n#Voltar')

def taxi():
    print('\n#Checklist')
    print('#Flow expandido(expandido)')
    print('#Adicional')
    print('\n#Voltar')

def bt():
    print('\n#Checklist - Antes de receber autorização(antes)')
    print('#Flow expandido - Antes(expandido antes)')
    print('#Checklist - Depois de receber autorização(depois)')
    print('#Flow expandido - depois(expandido depois)')
    print('#Adicionais')
    print('\n#Voltar')

def nt():
    print('\n#Generalidades')
    print('#Normal Takeoff Actions and Callouts(actions)')
    print('#After Takeoff Checklist')
    print('\n#Voltar')

def cruise():
    print('\n#Checklist')
    print('#Flow expandido(expandido)')
    print('#Adicionais')
    print('\n#Voltar')

def descent():
    print('\n#Checklist')
    print('#Flow expandido(expandido)')
    print('#Adicionais')
    print('\n#Voltar')

def pouso():
    print('\n#Tail Strike(tail)')
    print('#Hard Landing')
    print('#Bounced Landing(bounced)')
    print('#Pouso com vento de través')
    print('#Uso dos freios(freio)')
    print('\n#Voltar')

def landing_checklist():
    print('\n#Landing Checklist(landing)')
    print('#Aproximação estabilizada(aproximação)')
    print('#Pouso')
    print('\n#Voltar')

def landing():
    print('\n#Generalidades')
    print('#Checklist')
    print('#Flow expandido(expandido)')
    print('#Adicionais')
    print('\n#Voltar')
    querer = input('Qual informação você quer? ').lower()
    if querer == 'checklist':
        landing_checklist()

def al():
    print('\n#Checklist')
    print('#Flow expandido(expandido)')
    print('\n#Voltar')

def parking():
    print('\n#Checklist')
    print('#Flow expandido(expandido)')
    print('\n#Voltar')

def checklists():
    print('\n#Exterior Walkaround(exterior)')
    print('#Before start(bs)')
    print('#Engine Start(es)')
    print('#After Start(as)')
    print('#Táxi')
    print('#Before Takeoff(bt)')
    print('#Normal Takeoff(nt)')
    print('#Cruise')
    print('#Descent')
    print('#Go Around(ga)')
    print('#After Landing(al)')
    print('#Paring')
    print('#Securing')
    print('\n#Voltar')
    querer = input('Qual informação você quer? ').lower()
    if querer == 'exterior':
        exterior()
    elif querer == 'bs':
        bs()
    elif querer == 'es':
        es()
    elif querer == 'as':
        a_s()
    elif querer == 'taxi':
        taxi()
    elif querer == 'bt':
        bt()
    elif querer == 'nt':
        nt()
    elif querer == 'cruise':
        cruise()
    elif querer == 'descent':
        descent()
    elif querer == 'ga':
        um = 1
    elif querer == 'al':
        al()
    elif querer == 'parking':
        parking()
    elif querer == 'securing':
        um = 1

def briefings():
    print('\n#Briefing de Decolagem - TOSE (decolagem)')
    print('#Briefing de aproximação - ANFLACRAFTS(Aproximação)')
    print('#Briefing do aeroporto(aeroporto)')
    print('#Briefing Check the Glass ou The Glass (glass)')
    print('\n#Voltar')
    querer = input('Qual informação você quer? ').lower()

def filosofia_operacional():
    voltar = False
    info_lista = 0
    while not voltar:
        print('\n#Comunicação(com)')
        print('#Tranferência de Controle e Comunicações(transferencia)')
        print('#Utilização de Luzes Externas(luz)')
        print('\n#Voltar\n')
        querer = input('Qual informação você quer? ').lower()
        if querer == 'com':
            print('\nComunicação\n')
            print('A comunicação eficiente entre Aluno e Instrutor é vital para uma boa coordenação de cabine.')
            print('Sempre que um piloto receber informações atualizadas ou executar qualquer ajuste em um equipamento, deverá informar ao(à) outro(a) piloto e receber confirmação de ciência sobre a mudança em questão.')
        elif querer == 'transferencia':
            print('\nTransferência de Controle e Comunicações\n')
            for i in transferencia:
                print(transferencia[info_lista])
                info_lista += 1
            info_lista = 0
            print('AL: "Your Controls and ATC"','\nIN: "My Controls and ATC"')
            print('\nAL: "Your Controls, My ATC"','\nIN:"My controls, your ATC"')
            print('\nAL:"My controls and ATC"','\nIN: "Your controls and ATC"')
            print('\nAL: "My controls, your ATC"','\nIN: "Your controls, my ATC"')
        elif querer == 'luz':
            print('\nUtilização de Luzes Externas\n')
            for i in nav:
                print(nav[info_lista])
                info_lista += 1
            info_lista = 0
            for i in beacon:
                print(beacon[info_lista])
                info_lista += 1
            info_lista = 0
            for i in landing:
                print(landing[info_lista])
                info_lista += 1
            info_lista = 0
            for i in strobe:
                print(strobe[info_lista])
                info_lista += 1
            info_lista = 0
            print('\nNOTA\n')
            print('Durante backtrack, cruzamento e/ou taxi sobre a pista em uso, utilizar a configuração de luzes aplicável para a decolagem, e manter até que a pista seja completamente liberada.')
        elif querer == 'voltar':
            print('\nVoltar\n')
            voltar = True
            return voltar
        info_lista = 0

def adicionais():
    voltar = False
    info_lista = 0
    while not voltar:
        print('\n#Filosofia do SOP(SOP)')
        print('#Tripulação')
        print('#Filosofia de leitura do Checklist(checklist)')
        print('#Filosofia Operacional(operacional)')
        #NÃO FUNCIONANDO AINDA ----> print('#Flight Mode Annunciator(FMA)')
        #NÃO FUNCIONANDO AINDA ----> print('#Callouts')
        print('\n#Voltar\n')
        querer = input('Qual informação você quer? ').lower()
        if querer == 'sop':
            print('\nFilosofia do SOP (Standard Operanting Procedures)')
            for i in sop:
                print(sop[info_lista])
                info_lista += 1
        elif querer == 'tripulação':
            print('\nTripulação\n')
            for i in trip:
                print(trip[info_lista])
                info_lista += 1
        elif querer == 'checklist':
            print('\nFilosofia de leitura do Checklist\n')
            print('O uso correto dos Normal Checklists reduz a incidência de práticas inseguras, não padronizadas e/ou desenvolvimento de procedimentos informais.')
            for i in check:
                print(check[info_lista])
                info_lista += 1
            info_lista = 0
            print('O piloto deverá anunciar o nome do checklist antes de iniciar a sua leitura. Ao término, deverá anunciar o nome do checklist, seguido por "Complete"')
            print('Down the line/Below the line - Quando um checklist for segregado em dois momentos, o piloto deve anunciar "Down the Line" ao atingir a linha separadora. Para realizar a segunda parte do checklist, deve anunciar o "Below the Line"')
            for i in before_takeoff:
                print(before_takeoff[info_lista])
                info_lista += 1
            info_lista = 0
            print('\nA execução dos Normal Checklist deve ocorrer conforme o seguinte exemplo:')
            for i in execucao:
                print(execucao[info_lista])
                info_lista += 1
        elif querer == 'operacional':
            print('\nFilosofia Operacional\n')
            filosofia_operacional()
        elif querer == 'fma':
            print('\nFlight Mode Annunciator\n')
        elif querer == 'callouts':
            print('\nCallouts\n')
        elif querer == 'voltar':
            print('\nVoltar')
            voltar = True
            return voltar
        info_lista = 0

def curta():
    print('\n#Actions e Callouts(actions)')
    print('#Tabela de performance de decolagem curta(performance)')

def cold():
    print('\n#Formação de Gelo no Carburador(gelo)')
    print('#Utiliza da Tabela de Probabilidade de Formação de gelo(tabela)')
    print('#Em caso de suspeita de formação de gelo(suspeita)')

def procedimentos():
    print('\n#Táxi')
    print('#Acionamento Manual - Giro de Hélice(manual)')
    print('#Decolagem Curta ou pista em grama(curta)')
    print('#Performance de subida(subida)')
    print('#Consumo em Cruzeiro de Velocidade(consumo)')
    print('#Cold Weather Operation(cold)')
    print('#Dive and Drive')
    querer = input('Qual informação você quer? ').lower()
    if querer == 'curta':
        curta()
    elif querer == 'cold':
        cold()

def motor_aciona():
    print('\n#Motor acionado(acionado)')
    print('#Knocking under load(knocking)')
    print('#Motor áspero após período de aquecimento, emissão de fumaça pelo escapamento(aspero)')
    querer = input('Qual informação você quer? ').lower()

def emergência_oleo():
    print('\n#Baixa pressão')
    print('#Alta pressão')

def rotax():
    print('\n#Motor não aciona(não)')
    print('#Motor aciona(aciona)')
    print('#Pressão de Óleo (óleo)')
    print('#Nível de óleo(nivel)')
    print('#Acionamento frio do motor(frio)')
    querer = input('Qual informação você quer? ').lower()
    if querer == 'aciona':
        motor_aciona()
    elif querer == 'óleo':
        emergência_oleo()
    elif querer == 'nivel':
        um = 1

def emergência():
    print('\n#Geral')
    print('#Troubleshooting conforme ROTAX(ROTAX)')
    querer = input('Qual informação você quer? ').lower()
    if querer == 'rotax':
        rotax()

def montaer():
    sair = False
    while not sair:
        print('\nInformações disponíveis:')
        print('#Limites')
        #NÃO FUNCIONANDO AINDA ----> print('#Checklists')
        #NÃO FUNCIONANDO AINDA ----> print('#Briefings')
        print('#Formato de Leitura e informações adicionais(adicionais)')
        #print('#Procedimentos Adicionais e Performance(procedimentos)')
        #NÃO FUNCIONANDO AINDA ----> print('#Procedimentos anormais e de emergência(emergência)')
        print('#Sair\n')
        informação = input('Qual informação você quer? ').lower()
        if informação == 'limites':
            limites()
        elif informação == 'checklists':
            checklists()
        elif informação == 'briefings':
            briefings()
        elif informação == 'adicionais':
            adicionais()
        elif informação == 'procedimentos':
            procedimentos()
        elif informação == 'emergência':
            emergência()
        elif informação == 'sair':
            sair = True
            return sair

print('Bem-vindo! Aqui te ofereço algumas informações sobre a aeronave Montaer MC01')
sair = False
while not sair:
    x = montaer()
    if x == True:
        sair = True
if sair == True:
    print('\nTchau! Volte sempre!')
