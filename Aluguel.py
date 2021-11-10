diaria = []
kms = []
dias = []
Aluguel_7dias = []
pessoas_selecionadas = 0
#Comentar codigos
while True:
    nome = str(input('\nDigite seu nome (Digite "Sair" para fechar o codigo):')).capitalize()
    while nome.isnumeric():
        nome = str(input('\nDigite seu nome (Digite Sair para fechar o codigo)/Evitar números:')).capitalize()
    if nome == 'Sair':
        break
    sexo = str(input('Digite sua sexualidade (F-Feminino / M-Masculino):')).capitalize()
    while sexo not in ["F", "M"]:
        sexo = str(input('Digite sua sexualidade (F-Feminino / M-Masculino):')).capitalize()
    pessoas_selecionadas += 1
    placa = input('Digite a placa do sua carro:')
    while True:
        try:
            km = float(input('Quantidade de km contratados:'))
            if km >= 0:
                break
            elif km < 0:
                print('Algo está incorreto. Por fovor digite novamente!')
        except ValueError:
            print('Algo está incorreto. Por fovor digite novamente!')
    kms.append(km)
    while True:
        try:
            dia = int(input('Quantidade de dias contratados:'))
            if dia >= 0:
                break
            elif dia < 0:
                print('Algo está incorreto. Por fovor digite novamente!')
        except ValueError:
            print('Algo está incorreto. Por fovor digite novamente!')
    dias.append(dia)
    Aluguel = dia * 70 + km * 0.10
    diaria += [f'Placa {placa},Aluguel {Aluguel}']
    if dia > 7 and sexo == 'F':
        Aluguel_7dias += [f'Nome {nome}']
media = 0
try:
    media = (sum(kms)/pessoas_selecionadas)
except ZeroDivisionError:
    pass
print('Placa do carro e aluguel referente a cada cliente:')
for l in range(len(diaria)):
    print(diaria[l])
print(f'Media de quilometros contratados pelos clientes é igual {media}')
print('A quantidade de pessoas do sexo feminino com aluguel acima de 7 dias alugados é igual a:')
for f in range(len(Aluguel_7dias)):
    print(Aluguel_7dias[f])