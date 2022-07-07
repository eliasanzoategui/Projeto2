import scriptDeSaveELoad05 as ssl
import os
import criptografia1 as c1

class UnidadeDeSaveELoad():
    def __init__(self, caminho, numero, key):
        self.caminho = caminho
        self.numero = numero
        self.key = key
        if not ('banco_' + str(self.numero) + '.txt') in os.listdir(self.caminho):
            self.criar()
    def criar(self):
        arq = open(self.gerarBanco(), 'wb')
        arq.write(bytes([0]))
        arq.close()
    def salvarValores(self, valores):
        arquivo = open(self.gerarBanco(), 'wb')
        v = ssl.codificarValores(valores, self.key)
        arquivo.write(v)
        arquivo.close()
    def retornarValor(self, nome):
        nome = str(nome)
        arquivos = self.carregar()
        if arquivos == None:
            arquivos = []
        if ssl.seExisteValor(arquivos, nome):
            v = ssl.procurar(nome, arquivos).valores
            return v
    def retornarUmValor(self, nome, numero):
        nome = str(nome)
        arquivos = self.carregar()
        if arquivos == None:
            arquivos = []
        if ssl.seExisteValor(arquivos, nome):
            try:
                return ssl.procurar(nome, arquivos).valores[numero]
            except:
                pass
    def gerarBanco(self):
        return self.caminho + '\\banco_' + str(self.numero) + '.txt'
    def carregar(self):
        return ssl.decodificarValores(open(self.gerarBanco(), 'rb').read(), self.key)
    def salvarLista(self, nome, valor):
        arquivos = self.carregar()
        if arquivos == None:
            arquivos = []
        if ssl.seExisteValor(arquivos, nome):
            arquivo = ssl.procurar(nome, arquivos)
            arquivo = arquivo.mudarValor(valor)
        else:
            arquivo = ssl.ValorNoArquivo(nome, valor)
            arquivos.append(arquivo)
        self.salvarValores(arquivos)
    def inserirUmValor(self, nome, valor, numero):
        arquivos = self.carregar()
        if arquivos == None:
            arquivos = []
        if ssl.seExisteValor(arquivos, nome):
            arquivo = ssl.procurar(nome, arquivos)
            arquivo = arquivo.inserirUmValor(valor, numero)
        else:
            arquivo = ssl.ValorNoArquivo(nome, [valor])
            arquivos.append(arquivo)
        self.salvarValores(arquivos)
    def adicionarUmValor(self, nome, valor):
        arquivos = self.carregar()
        if arquivos == None:
            arquivos = []
        if ssl.seExisteValor(arquivos, nome):
            arquivo = ssl.procurar(nome, arquivos)
            arquivo = arquivo.adicionarUmValor(valor)
        else:
            arquivo = ssl.ValorNoArquivo(nome, [valor])
            arquivos.append(arquivo)
        self.salvarValores(arquivos)
    def retornarTodosOsNomesDosValores(self):
        nomes = []
        valores = self.carregar()
        for i in valores:
            nomes.append(i.nome)
        return nomes
    def removerUmValor(self, nome, numero):
        arquivos = self.carregar()
        if arquivos == None:
            arquivos = []
        if ssl.seExisteValor(arquivos, nome):
            arquivo = ssl.procurar(nome, arquivos)
            arquivo = arquivo.removerUmValor(numero)
        self.salvarValores(arquivos)
    def excluirValor(self, nome):
        valores = self.carregar()
        novosValores = valores
        for i in valores:
            if i.nome == nome:
                novosValores.remove(i)
        self.salvarValores(novosValores)
    def retornarTodosOsValores(self):
        nomes = self.retornarTodosOsNomesDosValores()
        valores = []
        for i in nomes:
            valores.append(self.retornarValor(i))
        saida = {}
        for i in range(len(nomes)):
            saida[nomes[i]] = valores[i]
        return saida
    def adicionarValor(self, valor):
        valores = []
        carregados = self.retornarTodosOsValores()
        for valor1 in carregados.keys():
            try:
                valores.append(int(valor1))
            except:
                pass
        x = 0
        while x in valores:
                x += 1
        self.salvarLista(str(x), valor)
    def retornarTodosOsValoresDosNumeros(self):
        valores = []
        carregados = self.retornarTodosOsValores()
        for valor1 in carregados.keys():
            try:
                valores.append(int(valor1))
            except:
                pass
        valoresFinal = []
        for i in valores:
            valoresFinal.append(self.retornarValor(str(i)))
        return valoresFinal
    def retornarTodosOsNumeros(self):
        valores = []
        carregados = self.retornarTodosOsValores()
        for valor1 in carregados:
            try:
                valores.append(int(valor1))
            except:
                pass
        return valores
    def filtrar(self, parametro):
        lista = []
        for i in self.retornarTodosOsNomesDosValores():
            valor = self.retornarValor(i)
            for e in valor:
                if parametro in e:
                    lista.append(i)
        return lista
    def AtualizarTodosOsValoresNumeros(self, novosValores):
        valoresAnteriores = self.retornarTodosOsNumeros()
        for valor in valoresAnteriores:
            self.excluirValor(str(valor))
        for novoValor in novosValores:
            self.adicionarValor(novoValor)


 





