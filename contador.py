print('Hello, seja bem-vindo ao melhor contador de convidados para sua festa! \n')

print('Eu sou um robo desenvolvido em Python e vou lhe ajudar, primeiro me informe quantas pessoas voce quer convidar \n')

x = int(input('Digite o numero de convidados:'))
y = []

i = 1

while i <= int(x):
    nome_do_convidado = input('Digite o nome do convidado #' + str(i) + ':')
    y.append(nome_do_convidado)
    i += 1

print('Serao', x, 'convidados!')

print('\nLista de convidados')
for convidado in y:
    print(convidado)
