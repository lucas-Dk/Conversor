#biblioteca usada
import time

#Variaveis de cáculo
dia = 24
minuto = 60
segundo = 3600
mensagem = 'Você saiu'
apresentacao = 'CONVERSOR DE DIAS EM HORAS'

#Função final
def final():
  print('\n'+mensagem.center(50))
#Repetição do programa inteiro

while True:
  #Presentação
  print('\033[32m==\033[m' * 30)
  print(f'\033[1;91m{apresentacao:^57}\033[m')
  print('\033[1;32m==\033[m' * 30)

#Pergunta a quantidade de dias para o usuário
  dias = float(input('\nInforme quantos dias e veja quantas horas tem: '))

#Pergunta para iniciar o cálculo
  saber = str(input('\nPara saber quantas horas digite D: ')).upper()[0]

#Validação
  while saber not in 'D':
    print('\n\033[1;91mOpção inválida!\033[m')
    saber = str(input('Para saber quantas horas digite D: ')).upper()[0]
  print('\nCalculando...')
  time.sleep(2)

#Caminhos de acordo com a escolha
  if saber.strip() == 'D':
    tempo = dias * dia
    print('\n\033[4m{:.0f}\033[m dias tem {:.0f} horas '.format(dias, tempo))
    valor = tempo

#Pergunta ao usuário
  minutos = str(input('\nQuer saber os minutos: [S/N]: ')).upper()[0]

#Validação
  while minutos not in 'S' and minutos not in 'N':
    print('\n\033[1;91mOpção inválida!\033[m')
    minutos = str(input('Quer saber os minutos: [S/N]: ')).upper()[0]

#Caminhos de acordo com a escolha
  if minutos.strip() == 'S':
    print('\nCalculando...')
    time.sleep(2)
    t = valor * minuto
    print('\n\033[4m{:.0f}\033[m dias tem {:.0f} minutos'.format(dias, t))

  elif minutos.strip() == 'N':
    print('\nVocê não quis saber os minutos!')

#Pergunta ao usuário
  segundos = str(input('\nDeseja saber quantos segundos tem o dia? [S/N]: ')).upper()[0]

#Validação
  while segundos not in 'S' and segundos not in 'N':
    print('\n\033[1;91mOpção inválida!\033[m')
    segundos = str(input('Deseja saber quantos segundos tem o dia? [S/N]: ')).upper()[0]

#Caminhos de acordo com a escolha
  if segundos.strip() == 'S':
    print('\nCalculando...')
    time.sleep(2)
    x = tempo * segundo
    print('\n\033[4m{:.0f}\033[m dias tem {:.0f} segundos'.format(dias, x))
  
  elif segundos.strip() == 'N':
    print('\nVocê não quis saber os segundos')

#Pergunta ao usuário 
  continuar = str(input('\nQuer saber mais? Y para sim F para sair [Y/F]: ')).upper()[0]

#Validação
  while continuar not in 'Y' and continuar not in 'F':
    print('\n\033[1;91mOpção inválida!\033[m')
    continuar = str(input('\nQuer saber mais? Y para sim F para sair [Y/F]: ')).upper()[0]

#Caminho que fecha o programa
  if continuar.strip() == 'F':
    break

#Chamada da função de encerramento
final()
