'''Faça as seguintes conversões de tempo.'''

numero = float(input('Digite o valor'))

convert = numero * 1440
convert_2 = numero * 60
convert_3 = numero * 60
convert_4 = numero * 24 
convert_5 = numero * 3600

print('O valor de dias em min é {}'.format(convert))
print('O valor de horas em min é {}'.format(convert_2))
print('O valor de minutos em segundos é {}'.format(convert_3))
print('O valor de dias em horas {}'.format(convert_4))
print('O valor de horas em sagundos é {}'.format(convert_5))