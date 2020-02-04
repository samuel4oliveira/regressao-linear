def regressao_linear(x, y):
   
    somaX = 0.0
    somaY = 0.0
    somaXY = 0.0
    somaXQuad = 0.0
    for i in range(len(x)):

        somaX += float(x[i])
        somaY += float(y[i])
        somaXY += float(x[i]) * float(y[i])
        somaXQuad += float(x[i]) ** 2

    #Determinando Alpha
    alpha = len(x) * somaXY - somaX * somaY
    alpha /= len(x) * somaXQuad - somaX ** 2

    mediaX = somaX / len(x)
    mediaY = somaY / len(y)
    #Determinando Beta
    beta = mediaY - alpha * mediaX

    #Determinando Y
    Y = []
    for i in range(len(x)):
        Y.append(alpha * x[i] + beta)
    return Y