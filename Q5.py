'''Uma ciclista parte da cidade A as 9h e chega a cidade B distamte 72Km de A as 13h. Determine a velocidade média dessa 
ciclista na viagem de A ate B, em km/h e em m/s'''

deslocamento = float(input('Digite o valor do deslocamento:'))
Tempo_inicial = float(input('Digite o valor da saída do local: '))
Tempo_final = float(input('digite o valor da chegada a o local: '))
variacao_de_tempo = Tempo_final - Tempo_inicial
Vm = deslocamento / variacao_de_tempo
convert = Vm / 3.6

print('A velocidade média do objeto em {}Km/h e em {}m/s'.format(Vm, convert))