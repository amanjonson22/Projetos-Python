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
            limites = ['Máximo componente de vento de través: ', 'Decolagem/Pouso em voo duplo comando - 13 kt', 'Decolagem/Pouso em voo solo de aluno PCA - 08 kt', 'Decolagem/Pouso em voo solo de aluno PPA - 06 kt', 'Máx. componente de cauda para decolagem/pouso - 10 kt']
            for i in limites:
                print(limites[info_lista])
                info_lista += 1
        elif querer == 'combustível':
            print('\nCombustível')
            print('Combustível utilizável por tanque - 68L\n')
        elif querer == 'óleo':
            print('\nÓleo\n')
            óleo = ['Volume mínimo - 2,5 L', 'Pressão máxima - 102 psi', 'Pressão normal - 29 a 73 psi', 'Pressão mínima - 12 psi', 'Temperatura máxima - 130°C', 'Temperatura desejável - 90°C a 110°C', 'Temperatura mínima - 50°C']
            for i in óleo:
                print(óleo[info_lista])
                info_lista += 1
        elif querer == 'vc':
            print('\nVelocidades Características\n')
            velocidades = ['Máx. estrutural (VNE) - 117 kt', 'Máx. operacional (VNO)- 107 kt', 'Máx. de manobra (VA) - 88 kt', 'Máx. para operação Full flap (VFE) - 78 kt', 'Velocidade de estol sem flap (Vs) - 45kt', 'Velocidade de estol com flap 1 (Vs1) - 40kt', 'Velocidade de estol com flap 2 (Vs0) - 39kt', 'Velocidade melhor razão de subida (Vy) - 65kt', 'Velocidade melhor ângulo de subida (Vx) - 55kt', 'Velocidade de melhor planeio (Vg) - 60kt']
            for i in velocidades:
                print(velocidades[info_lista])
                info_lista += 1
        elif querer == 'motor':
            print('\nMotor\n')
            motor = ['Potência máxima (5.800 RPM) - 98,5 hp', 'Potência Max Continua (5.500 RPM) - 90 hp', 'Temperatura Máx. Coolant - 120°C', 'Temperatura máxima CHT - 135°C']
            for i in motor:
                print(motor[info_lista])
                info_lista += 1
        info_lista = 0

def checklists():
    um = 1

def briefings():
    um = 1 


def montaer():
    sair = False
    while not sair:
        print('\nInformações disponíveis:')
        print('#Limites')
        print('#Checklists')
        print('#Briefings')
        print('#Sair\n')
        informação = input('Qual informação você quer? ').lower()
        if informação == 'limites':
            limites()
        elif informação == 'checklists':
            checklists()
        elif informação == 'briefings':
            briefings()
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
