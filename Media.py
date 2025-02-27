notaA = float(input('Informe a primeira nota:'))
notaB = float(input('informe a segunda nota:'))

mediaFinal = (notaA + notaB) / 2

if mediaFinal >= 7.0:
    print('A média: %.1f - Aprovado' % mediaFinal)
else:
    print('A média: %.1f - Reprovado' % mediaFinal)