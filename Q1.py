'''Transformes as unidades de medida de comprimento.'''

numero = float(input('Digite o valor'))

convert = numero * 1000
convert_2 = numero * 100
convert_3 = numero * 10
convert_4 = numero *100000
convert_5 = numero *1000000

print('Valor em {}m'.format(convert))
print('Valor em {}cm'.format(convert_2))
print('Valor em {}mm'.format(convert_3))
print('Valor em Km e {}cm'.format(convert_4))
print('Valor em Km e {}mm'.format(convert_5))