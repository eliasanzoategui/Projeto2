import random
import Banco06 as b1
import math as m1







class DataBase():
    def __init__(self, caminho, numero):
        self.banco = b1.UnidadeDeSaveELoad(caminho, numero)
    def adicionarDado(self, dado):
        self.banco.adicionarValor(dado)
    def filtrar(self, entradas, resultados):
        in1 = []
        out1 = []
        valores = self.banco.retornarTodosOsValoresDosNumeros()
        for n1 in range(len(valores)):
            try:
                dado = []
                for n2 in entradas:
                    dado.append(float(valores[n1][n2]))
                in1.append(dado)
                dado = []
                for n2 in resultados:
                    dado.append(float(valores[n1][n2]))
                out1.append(dado)
            except:
                print('Erro')

        dadosFiltrados = []
        for n1 in range(len(in1)):
            dadosFiltrados.append(Data(in1[n1], out1[n1]))
        return dadosFiltrados





















class DicionarioRna():
    def  __init__(self, vocabulario):
        self.vocabulario = vocabulario
    def ler(self, texto):
        palavrasText = texto.split(' ')
        palavrasChave = 0
        palavras = [0] * len(self.vocabulario)
        for n1 in range(len(self.vocabulario)):
            palavras[n1] = palavrasText.count(self.vocabulario[n1])

        for n1 in palavrasText:
            if n1 not in self.vocabulario:
                palavrasChave += 1
        return palavras + [palavrasChave]




class FunçõesBasicasNeurais():
    def __init__(self):
        pass
    def retornarDados(self, dados):
        entradas = []
        resultados = []
        for num in range(len(dados)):
            entradas.append(dados[num].retornarEntrada())
            resultados.append(dados[num].retornarResultado())
        return [entradas, resultados]
    def functionDegral(self, saida):
        if saida > 0:
            return 1
        else:
            return 0
    def functioSigmoid(self, x):
        return 1 / (1 + m1.exp(-x))
    def functionNum(self, x):
        return x
    def positivo(self, x):
        if x < 0:
            x= -x
        return x
    def porcentagemDeErro(self, resultados, erro):
        total = len(resultados[0]) * len(resultados)
        return (total - erro) / total
    def somaDosErros(self, saidas, resultados):
        erro = 0
        for i in range(0, len(resultados)):
            erro += self.positivo(saidas[i] - resultados[i]) ** 2
        return erro
    def listar(self, rede, dados):
        entradas, resultados = self.retornarDados(dados)
        for i in range(len(entradas)):
            print(entradas[i], ':', rede.usar(dados[i]))


class SaveLoadRedeBasico():
    def __init__(self):
        pass
    def codificarNeuronio(self, neuronio):
        cod = ''
        for i in neuronio.pesos:
            cod += str(i) + 'w'
        cod += str(neuronio.bias) + 'zn'
        return cod
    def codificarCamada(self, camada):
        cod = ''
        for i in camada.neuronios:
            cod += self.codificarNeuronio(i)
        return cod + 'c'
    def codificarRede(self, rede):
        cod = ''
        for i in rede.camadas:
            cod += self.codificarCamada(i)
        return cod + 'r'
    def codificar(self, redes):
        cod = []
        for i in redes:
            cod.append(self.codificarRede(i))
        return cod
    def decodificar(self, texto):
        camadas = []
        neuronios = []
        pesos = []
        bias = 0
        valor = ''
        for caractere in texto:
            if caractere == 'w':
                pesos.append(float(valor))
                valor = ''
            elif caractere == 'z':
                bias = float(valor)
                valor = ''
            elif caractere == 'n':
                neuronios.append(NeuronioIntegrado().receber(pesos, bias))
                pesos = []
                bias = 0
            elif caractere == 'c':
                camadas.append(CamadaIntegrada().receber(neuronios))
                neuronios = []
            elif caractere == 'r':
                rede = RedeNeuralIntegrada().receber(camadas)
                camadas = []
            else:
                valor += caractere
        return rede






































class Data():
    def __init__(self, entrada, resultado):
        self.entrada = entrada
        self.resultado = resultado
    def retornarEntrada(self):
        return self.entrada
    def retornarResultado(self):
        return self.resultado
    def retornarPeso(self):
        return self.peso








class Neuron():
	def processar(self, entrada):
		return self.processarDados(entrada)	
	def receber(self, pesos, bias):
		self.pesos = pesos
		self.bias = bias
		return self
	def gerar(self, pesos):
		self.gerarPesos(pesos)
		return self
	def mutar(self, taxa):
		self.mutateWheigths(taxa)
	def aleatoriar(self):
		self.aleatoriarPesos()
	def adicionarPeso(self):
		self.pesos.append(0)



class NeuronioIntegrado(Neuron):
    def __init__(self):
        self.taxa = 1
        self.lim = 1000
    def processarDados(self, entradas, ativação):
        saida = 0
        for i in range(len(self.pesos)):
            saida += entradas[i] * self.pesos[i]
        saida += self.bias
        return ativação(saida)
    def gerarPesos(self, pesos):
        self.pesos = []
        self.bias = self.bias = round(random.randint(-self.lim, self.lim), 4)
        for i in range(pesos):
            self.pesos.append(round(random.randint(-self.lim, self.lim), 4))
        return self
    def mutateWeights(self, taxa):
        for i in range(len(self.pesos)):
            self.pesos[i] += taxa * self.taxa
            if self.pesos[i] > self.lim:
                self.pesos[i] = self.lim
            if self.pesos[i] < -self.lim:
                self.pesos[i] = -self.lim
            self.pesos[i] = round(self.pesos[i], 4)
        self.bias += taxa * self.taxa
        if self.bias > self.lim:
            self.bias = self.lim
        if self.bias < -self.lim:
            self.bias = -self.lim
        self.bias = round(self.bias, 4)
    def aleatoriarPesos(self):
        for i in range(len(self.pesos)):
            self.pesos[i] = random.randint(-self.lim, self.lim)
            self.pesos[i] = round(self.pesos[i], 4)
        self.bias = random.randint(-self.lim, self.lim)
        self.bias = round(self.bias, 4)



class Camada():
	def receber(self, neuronios):
		self.neuronios = neuronios
		return self
	def gerar(self, neuronios, entradas):
		self.gerarNeuronios(neuronios, entradas)
		return self
	def processar(self, entrada):
		return self.processarDados(entrada)
	def taxa(self, taxa):
		self.mutarNeuronios(taxa)
	def aleatoriar(self):
		self.aleatoriarNeuronios()


class CamadaIntegrada(Camada):
	def gerarNeuronios(self, neuronios, entradas):
		self.neuronios = []
		for i in range(neuronios):	
			self.neuronios.append(NeuronioIntegrado().gerarPesos(entradas))
		return self
	def processarDados(self, entrada, ativação):
		saidas = []
		for i in range(0, len(self.neuronios)):
			saidas.append(self.neuronios[i].processarDados(entrada, ativação))
		return saidas
	def mutarNeuronios(self, taxa):
		for i in self.neuronios:
			i.mutateWeights(taxa)
	def aleatoriarNeuronios(self):
		for i in self.neuronios:
			i.aleatoriarPesos()



class RedeNeural():
	def receber(self, camadas):
		self.camadas = camadas
		return self
	def gerar(self, camadas, entrada):
		self.gerarCamadas(camadas, entrada)
		return self
	def processar(self, entrada, ativação):
		return self.processarDados(entrada, ativação)
	def mutar(self, taxa):
		self.mutarCamadas(taxa)
	def aleatoriar(self):
		self.aleatoriarCamadas()
	def retornarErros(self, entradas, resultados, ativação):
		return self.retornarErrosCamadas(entradas, resultados, ativação)


class RedeNeuralIntegrada(RedeNeural):
    def mutarCamadas(self, taxa):
        for i in self.camadas:
            i.mutarNeuronios(taxa)
    def aleatoriarCamadas(self):
        for i in self.camadas:
            i.aleatoriarNeuronios()
    def retornarErrosCamadas(self, entradas, resultados, ativação):   
        erro = 0
        for i in range(len(entradas)):    
            erro += FunçõesBasicasNeurais().somaDosErros(self.processarDados(entradas[i], ativação),resultados[i])
        return erro
    def gerarCamadas(self, camadas, entrada):
        self.camadas = [CamadaIntegrada().gerarNeuronios(camadas[0], entrada)]
        self.entrada = entrada
        for i in range(1, len(camadas)):
            self.camadas.append(CamadaIntegrada().gerarNeuronios(camadas[i], camadas[i - 1]))
        return self
    def processarDados(self, entrada, ativação):
        saidas = self.camadas[0].processarDados(entrada, ativação)
        for i in range(1, len(self.camadas)):
            saidas = self.camadas[i].processarDados(saidas, ativação)
        return saidas


class FunçõesBasicasRna():
    def salvar(self, rede):
        self.banco.banco.salvarLista(self.nome, SaveLoadRedeBasico().codificar([rede]))
    def excluir(self):
        self.banco.banco.excluirValor(self.nome)
    def retornarErrosCamadas(self, peso, entradas, resultados):
        return self.rede.retornarErrosCamadas(peso, entradas, resultados, self.ativação)
    def adicionarDado(self, dado):
        self.banco.adicionarDado(dado)
    def adicionarDados(self, dados):
        for dado in dados:
            self.banco.adicionarDado(dado)
    def listar(self, entradas, resultados):
        for i in self.banco.filtrar(entradas, resultados):
            print('entrada: ', i.entrada, '/Resultado: ', i.resultado, '->', self.usar(i.entrada))



class Rna(RedeNeuralIntegrada, FunçõesBasicasRna):
    def __init__(self, caminho, numero, parametros):
        self.ativação = FunçõesBasicasNeurais().functionDegral
        self.nome = 'rede neural'
        self.banco = DataBase(caminho, numero)
        self.população = 100
        self.neuronios = parametros[0]
        self.camadas = parametros[1]
        self.saidas = parametros[2]
        self.entradas = parametros[3]
    def usar(self, entrada):
        try:
            self.carregar()
            return self.rede.processar(entrada, self.ativação)
        except:
            print('Erro em usar rede neural')
    def treinar(self, lim, taxa, entradas, resultados):
        try:
            entradas, resultados = FunçõesBasicasNeurais().retornarDados(self.banco.filtrar(entradas, resultados))
            self.carregar()
            n1 = self.rede    
            e1 = n1.retornarErrosCamadas(entradas, resultados, self.ativação)
            print(e1)
            print('0%')
            for n in range(lim):   
                print(str(int(round((n / lim) * 100, 0))) + '%')
                e1 = self.flip(entradas, resultados, taxa, e1)
            print('100%')
        except:
            print('Erro de treino')
    def criar(self, parametros):
        self.neuronios = parametros[0]
        self.camadas = parametros[1]
        self.saidas = parametros[2]
        self.entradas = parametros[3]
        self.rede = self.gerar(self.camadas * [self.neuronios] + [self.saidas], self.entradas)
        self.salvar(self.rede)
    def carregar(self):
        try:  
            self.rede = SaveLoadRedeBasico().decodificar(self.banco.banco.retornarValor(self.nome)[0])
        except:
            print('Erro de carregamento da rede neural')
    def flip(self, entradas, resultados, taxa, e1):
        n1 = self.rede
        for n in range(self.população):
            n2 = n1
            n2.mutar(e1 * taxa)
            e2 = n2.retornarErrosCamadas(entradas, resultados, self.ativação)
            if e2 < e1:
                n1 = n2
                e1 = e2
        n2 = self.rede
        n2.aleatoriar()
        e2 = n2.retornarErrosCamadas(entradas, resultados, self.ativação)
        if e2 < e1:
            self.rede = n2
            e1 = e2
            self.salvar(n1)
        return e1



