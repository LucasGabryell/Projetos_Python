def nascimento(dia,mes,ano):
    Meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO',
             'SETEMBRO', 'OUTUBRO', 'NOVEMBRO','DEZEMBRO']
    return f'{dia}/{Meses[mes - 1]}/{ano}'
while True:
    try:
        dia = int(input('Digite o dia do nascimento:'))
        if dia <= 31:
            break
        if dia > 31:
            print('Quantidades de dias inexistentes em um mês!')
    except ValueError:
        print('Algo esta errado! Digite novemente.')
while True:
    try:
        mes = int(input('Digite o mês do nascimento:'))
        if mes <= 12:
            break
        if dia > 12:
            print('Quantidade de meses inexistente em um ano!')
    except ValueError:
        print('Algo esta errado! Digite novemente.')
while True:
    try:
        ano = int(input('Digite o Ano do nascimento:'))
        if ano <= 2021:
            break
        if ano > 2021:
            print('Voce ainda nao nasceu!')
    except ValueError:
        print('Algo esta errado! Digite novemente.')
print(nascimento(dia,mes,ano))