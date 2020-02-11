dado1 = open(r"C:\Users\samuel\Documents\ufmt\regressaoLinear\y.txt", 'r').read()
dado2 = open(r"C:\Users\samuel\Documents\ufmt\regressaoLinear\x1.txt", 'r').read()
dado3 = open(r"C:\Users\samuel\Documents\ufmt\regressaoLinear\x2.txt", 'r').read()

y = dado1.split()
x1 = dado2.split()
x2 = dado3.split()

mediaY = 0.0
mediaX1 = 0.0
mediaX2 = 0.0
for i in range(len(y)):
    print(x1[i], "    ", x2[i], "    ", y[i])
    mediaY += float(y[i]) / len(y)
    mediaX1 += float(x1[i]) / len(y)
    mediaX2 += float(x2[i]) / len(y)

desvioPadraoY = 0.0
desvioPadraoX1 = 0.0
desvioPadraoX2 = 0.0
desvioPadraoX1Y = 0.0
desvioPadraoX2Y = 0.0
desvioPadraoX1X2 = 0.0
for i in range(len(y)):
    desvioPadraoY += (float(y[i]) - mediaY) ** 2
    desvioPadraoX1 += (float(x1[i]) - mediaX1) ** 2
    desvioPadraoX2 += (float(x2[i]) - mediaX2) ** 2
    desvioPadraoX1X2 += (float(x1[i]) - mediaX1) * (float(x2[i]) - mediaX2)
print(desvioPadraoX1X2)