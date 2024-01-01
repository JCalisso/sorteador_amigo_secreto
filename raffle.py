import os
from random import randint
from sys import platform

from email_sender import send_email

## Preenche a lista de amigos que vão participar do sorteio
qtd_amigos = 8


amigos = [
    {'id': 1, 'nome': 'Jean Calisso', 'email': 'jv.calisso@gmail.com'},
    {'id': 2, 'nome': 'Vitória Gava', 'email': 'vickgava@gmail.com'},
    {'id': 3, 'nome': 'Ronaldo', 'email': 'ronaldohenriquenado@gmail.com'},
    {'id': 4, 'nome': 'Maria Almeida', 'email': 'marialmeidapb2000@gmail.com'},
    {'id': 5, 'nome': 'Letícia Berti', 'email': 'leticiarbds@icloud.com'},
    {'id': 6, 'nome': 'Fernando Berti', 'email': 'bertifernando50@gmail.com'},
    {'id': 7, 'nome': 'Miguel', 'email': 'miguelspinelnet@gmail.com'},
    {'id': 8, 'nome': 'Bia Nunes', 'email': 'Thomazbia18@gmail.com'},
    ]

## Inicializa a lista onde ficará o resultado do sorteio
sorteio = []

def sortear(sorteando, amigos, sorteados, sorteio, contador):
    ## Verifica se a quantidade de chamadas recursivas não está próxima
    ## de ultrapassar a quantidade máxima
    ## Se estiver, retornamos False para recomeçar o sorteio
    contador += 1
    if contador > 900:
        return False
    
    ## Sorteia um amigo
    sorteado = amigos[randint(0, qtd_amigos-1)]


    ## Verifica se o amigo sorteado já não foi sorteado por outro
    requisito_1 = (sorteado['id'] in sorteados)
    ## Verifica se o amigo sorteado já não sorteou quem o está sorteando
    ## Só evita aquelas coisas chatas de um sair com o outro e o outro com o um
    ## É opcional, você pode remover :)
    requisito_2 = ([x for x in sorteio if x['sorteante'] == sorteando['id'] and \
    x['sorteado'] == sorteando['id']])
    ## Verifica se quem sorteia não sorteou ele mesmo
    requisito_3 = (sorteado['id'] == sorteando['id'])

    if (requisito_1 or requisito_2 or requisito_3):
        ## Se qualquer um dos requisitos acima for verdadeiro
        ## realiza-se o sorteio novamente até que encontre um resultado satisfatório
        sortear(sorteando, amigos, sorteados, sorteio, contador)
    else:
        ## Se não, adicionamos o resultado do sorteio na lista de resultados
        sorteio.append({'sorteante': sorteando['id'], 'sorteado':sorteado['id']})
        return True
    

## Enquanto a função sortear retornar False e não tiver um sorteio satisfatório
## o sorteio será realizado novamente
while len(sorteio) != qtd_amigos:
    sorteio = []
    for rodada in range(qtd_amigos):
        ## O sorteio é feito um por um e sempre conferido

        sorteados = [x['sorteado'] for x in sorteio]
        ## Contador de chamadas recursivas
        contador = 0

        sortear(amigos[rodada], amigos, sorteados, sorteio, contador)

## Divulga o resultado do sorteio
for rodada in sorteio:
    for amigo in amigos:
        if rodada['sorteante'] == amigo['id']:
            sorteante = amigo['nome']
            email_sorteante = amigo['email']
        elif rodada['sorteado'] == amigo['id']:
            sorteado = amigo['nome']

    send_email(sorteante, email_sorteante, sorteado)


