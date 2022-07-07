import criptografia1 as c1


def procurar(nome, valores):
    for i in valores:
        if i.nome == nome:
            return i

def decodificarValores(texto, key):
    nome = ''
    valor = ''
    adicionarAoValor = False
    valores = []
    lista = []
    texto = c1.t1(c1.l0(texto, key, 0))
    for caractere in texto:
        if caractere == ',' and adicionarAoValor:
            lista.append(valor)
            valor = ''
            continue
        if caractere == '\n':
                continue
        if caractere == ']':
            lista.append(valor)
            valores.append(ValorNoArquivo(nome, lista))
            valor = ''
            nome = ''
            lista = []
            adicionarAoValor = False
            continue

        if caractere == '[':
            adicionarAoValor = True
            continue

        if adicionarAoValor:
            valor += caractere
        else:
            nome += caractere


    return valores

def codificarValores(valores, key):
    cod = ''
    for i in valores:
        cod += i.codificar() + '\n'
    cod = c1.t2(cod)
    return c1.l0(cod, key, 1)

class ValorNoArquivo():
    def __init__(self, nome, valores):
        self.nome = nome
        self.valores = valores
    def retornarValor(self):
        return self.valores
    def retornarUmValor(self, numero):
        if numero < len(self.valores):
            return self.valores[numero]
    def codificar(self):
        saida = str(self.nome) + '['
        for r in range(len(self.valores)):
            if r < len(self.valores) - 1:
                saida += str(self.valores[r]) + ','
            else:
                saida += str(self.valores[r]) + ']'
        return saida
    def mudarValor(self, novoValor):
        self.valores = novoValor
    def inserirUmValor(self, novoValor, numero):
        if numero <= len(self.valores):
            self.valores.insert(numero, novoValor)
        else:
            self.valores.append(novoValor)
    def removerUmValor(self, index):
        try:
            self.valores.pop(index)
        except:
            pass
    def adicionarUmValor(self, valor):
        self.valores.append(valor)
    


def seExisteValor(arquivos, nome):
    if procurar(nome, arquivos) != None:
        return True
    else:
        return False


