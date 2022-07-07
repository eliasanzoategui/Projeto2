






class RegreçãoLinear():
    def somatórioLista(self, lista, expoente):
        valorTotal = 0
        for valor in lista:
            valorTotal += valor ** expoente
        return valorTotal
    def somatórioListas(self, lista1, lista2):
        valorTotal = 0
        for n in range(len(lista1)):
            valorTotal += lista1[n] * lista2[n]
        return valorTotal
    def relação(self, pontos, variáveis): # verifica a relação da reta em comparação ao gráfico
        pontos = self.listar(pontos, variáveis)
        v1 = variáveis[0]
        v2 = variáveis[1]
        sumx = self.somatórioLista(pontos[v1], 1)
        sumx2 = self.somatórioLista(pontos[v1], 2)
        sumy = self.somatórioLista(pontos[v2], 1)
        sumy2 = self.somatórioLista(pontos[v2], 2)
        sumxy = self.somatórioListas(pontos[v1], pontos[v2])
        n = len(pontos[v1])
        return (sumxy * n - sumx * sumy) / ((n * sumx2 - (sumx) ** 2) ** 0.5 * (n * sumy2 - (sumy) ** 2) ** 0.5)
    def regressão(self, pontos, variáveis): # calcula a reta
        pontos = self.listar(pontos, variáveis)
        v1 = variáveis[0]
        v2 = variáveis[1]
        sumx = self.somatórioLista(pontos[v1], 1)
        sumx2 = self.somatórioLista(pontos[v1], 2)
        sumy = self.somatórioLista(pontos[v2], 1)
        sumxy = self.somatórioListas(pontos[v1], pontos[v2])
        n = len(pontos[v1])
        a = (n * sumxy - sumx * sumy) / (n * sumx2 - sumx ** 2)
        b = (sumy - a * sumx) / n
        return [a, b]
    def previsão(self, reta, x):
        return reta[0] * x + reta[1]
    def listar(self, pontos, variaveis):
        x = []
        y = []
        for n in pontos:
            x.append(n.posição[variaveis[0]])
            y.append(n.posição[variaveis[1]])
        return {variaveis[0]:x, variaveis[1]:y}

class Ponto():
    def __init__(self, posições):
        self.posição = posições
    









