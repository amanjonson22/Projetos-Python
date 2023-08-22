#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
#Se a pessoa responder positivamente: 
#a 2 questões ela deve ser classificada como "Suspeita", 
#entre 3 e 4 como "Cúmplice" e 
#5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

l = []
print ('Responda Sim(S) ou Não(N)')

p1 = input('Telefonou para a vítima? ').lower()
if p1 == 's':
    l.append(1)
else:
    l.append(0)

p2 = input('Esteve no local do crime? ').lower()
if p2 == 's':
    l.append(1)
else:
    l.append(0)

p3 = input('Mora perto da vítima? ').lower()
if p3 == 's':
    l.append(1)
else:
    l.append(0)

p4 = input('Devia para a vítima? ').lower()
if p4 == 's':
    l.append(1)
else:
    l.append(0)

p5 = input('Já trabalhou com a vítima? ').lower()
if p5 == 's':
    l.append(1)
else:
    l.append(0)

crime = 0
numero = 0
for i in l:
    crime = crime + i
    numero += 1

if crime < 2:
    print('Inocente')

elif crime == 2:
    print('Suspeito')

elif crime == 3 or crime == 4:
    print('Cúmplice')

elif crime == 5:
    print('Assassino')
