velocidade_maxima = 100
if velocidade <= (velocidade_maxima * 20) / 100 + velocidade_maxima:
  print('Sem infração! Parabéns, não fez mais do que sua obrigação.')
elif velocidade > velocidade_maxima  and velocidade <= (velocidade_maxima * 40) / 100 + velocidade_maxima:
  print('Infração média:R$ 130,16 - 4 pontos ')
elif velocidade > (velocidade_maxima * 40) / 100 + velocidade_maxima and velocidade <= (velocidade_maxima * 70) / 100 + velocidade_maxima:
  print('Infração grave: 195,23 - 5 pontos')
elif velocidade > (velocidade_maxima * 70) / 100 + velocidade_maxima:
  print('Infração gravissima: 880,41 - 7 pontos')