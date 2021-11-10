def Convercao (horas,minutos):
        if horas < 12:
            horas24 = 12
        else:
            horas24 = horas - 12
        return str(horas24) + ":" + str(minutos)
def Saida ():
    AMPM = 'AM' if horas < 12 else "PM"
    return AMPM
while True:
    continuar = input('Digite "S" para CONTINUAS e "N" para SAIR:').upper()
    while continuar.isnumeric():
        continuar = input('Digite "S" para CONTINUAS e "N" para SAIR // EVITAR NUMEROS! :').upper()
    if continuar in ('S','N'):
        if continuar == 'N':
            break
        if continuar == 'S':
            while True:
                try:
                    horas = int(input('DIGITE AS HORAS:'))
                    if horas > 24:
                        print('Qauntidade de horas inexistentes em um dia!')
                    if horas < 24:
                        break
                except ValueError:
                    print('Algo esta errado, Digite novamente!')
            while True:
                try:
                    minutos = int(input('DIGITE OS MINUTOS:'))
                    if minutos > 59:
                        print('Algo esta errado, Digite novamente!')
                    if minutos < 60:
                        break
                except ValueError:
                    print('Algo esta errado, Digite novamente!')
            print(Convercao(horas,minutos)+Saida())


