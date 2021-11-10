questoes = []
gabarito_lista = ['A','C','D','E','A','B','B','E','C','A']
respostas = []
Respostas_Corretas = 0
Respostas_Erradas = 0
#foi utilizado do isnumeric para filtrar apenas letras no codigo, excluindo numeros
#fiz tambem um apanhado de apenas letras de A ate E, sendo ela as unicas aceitas
#usei do for para printar os alunos e suas respectivas questões
while True:
    nome = str(input('\nDigite seu nome (Digite "Sair" para fechar o codigo):')).capitalize()
    while nome.isnumeric():
        nome = str(input('\nDigite seu nome (Digite Sair para fechar o codigo)/Evitar números:')).capitalize()
    if nome == 'Sair':
        break
    sexo = str(input('Digite sua sexualidade (F-Feminino / M-Masculino):')).capitalize()
    while sexo not in ["F", "M"]:
        sexo = str(input('Digite sua sexualidade (F-Feminino / M-Masculino):')).capitalize()
    for k in range(1,11):
        print('Digite A, B, C, D ou E para responder!')
        questao = 0
        while questao not in ["A", "B", "C", "D", "E"]:
            questao = str(input('Digite sua resposta(Apenas respostas '
                                'contendo as letras acima serão computadas:')).upper()
            respostas.append(questao)
    for v in range(0, len(respostas)):
        if respostas[v] == gabarito_lista[v]:
            Respostas_Corretas += 1
        else:
            Respostas_Erradas += 1
    questoes += [f'Aluno {nome}, Sexo {sexo}, Respostas correstas: {Respostas_Corretas}, Respostas Erradas: {Respostas_Erradas}']
    Respostas_Corretas = 0
    Respostas_Erradas = 0
    respostas.clear()
for l in range(0, len(questoes)):
    print(questoes[l])
