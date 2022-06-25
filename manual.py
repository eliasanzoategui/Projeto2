import criptografia2 as c1





def codificar(mensagem, chave):
    return c1.l0(mensagem, chave, True)

def decodificar(codigo, chave):
    return c1.l0(codigo, chave, False)



def passo1(primo, inteiro, númeroPrivado): # diffie-hellman passo1
    return c1.c1(primo, inteiro, númeroPrivado) # resultado

def passo2(primo, resultadoRecebido, númeroPrivado):
    return c1.c1(primo, resultadoRecebido, númeroPrivado)







def manual1(): # chave de codificação
    chave = b'abacaxi123'
    mensagem = b'hello world'
    codigo = codificar(mensagem, chave)
    inverso = decodificar(codigo, chave)
    print(codigo)
    print(inverso)

def manual2(): # chave errada
    chave = b'abacaxi123'
    mensagem = b'hello world'
    codigo = codificar(mensagem, chave)
    inverso = decodificar(codigo, chave)
    print(codigo)
    print(inverso)

    chaveErrada = b'bacaximalvado'
    print(decodificar(codigo, chaveErrada))


def diffieHelman(): # passo a passo
    primo = 17
    inteiro = 24
    
    # só um exemplo porque o código pode demorar para executar

    privado1 = 4
    privado2 = 5

    resultado1 = passo1(primo, inteiro, privado1)
    resultado2 = passo1(primo, inteiro, privado2)

    print('resultado1:', resultado1)
    print('resultado2:', resultado2)

    chave1 = passo2(primo, resultado2, privado1)
    chave2 = passo2(primo, resultado1, privado2)

    print('chave1:', chave1)
    print('chave2:', chave2)





