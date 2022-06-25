






def l1(b): # transforma bytes em uma [lista de inteiros >= 0 and < 256]
    return list(b)

def l2(b): # transforma uma [lista de inteiros >= 0 and < 256] em bytes
    return bytes(b)

def l3(m, n): # função módulo. essa função faz o módulo [m] do número [n] 
    while n < 0 or n >= m:
        if n < 0:
            n += m
        if n >= m:
            n -= m
    return n

def l0(code, key, command): # codifica os bytes [code] com a chave [key]
    if command:    # se o command é True a chave codifica
        command = 1
    else: # se o command é False a chave descodifica
        command = -1
    a0 = len(code)
    a1 = len(key)
    a2 = 0
    code = l1(code)
    key = l1(key)
    for n1 in range(a0):
        if a2 >= a1:
            a2 = 0
        code[n1] = l3(256, key[a2] * command + code[n1])
        a2 += 1
    return l2(code) # retorna bytes



def c1(p, i, n): # método diffie-hellman em que [p] == primo, [i] == inteiro, [n] == número
    return l3(p, i ** n) # [i] é elevado a [n] módulo [p]

def p1(n): # retorna se o número é primo
    r = int(n ** 0.5)
    if n == 2:
        return False
    for v in range(2, r + 1):
        if n % v == 0:
            return False
    return True

def b1(n): # transforma número inteiro em uma string de '0' e '1' binária
    v = ''
    while n > 0:
        n1 = n / 2
        if n1 == int(n1):
            v += '0'
        else:
            v += '1'
        n = int(n1)
    return v


def b2(b): # transforma uma string de '0' e '1' binária em um número inteiro
    s1 = 0
    for n in range(8):
        s1 += 2 ** n * int(b[n])
    return s1

def b3(l): # preenche uma sequência de 8 caracteres de uma string binária
    b = ''
    l1 = len(l)
    for n in range(8):
        if n >= l1:
            b += '0'
        else:
            b += l[n]
    return b

def b4(b): # separa uma sequência de uma string binária em uma sequência de 8 bit cada item
    s0 = []
    while b:
        s0.append(b2(b3(b)))
        b = b[8:]    
    return s0

def b0(n): # retorna uma sequência de 8 bit, cada item, de um número inteiro
    return b4(b1(n))




def h0(b): # faz o hash de um número binário
    a0 = 128
    a1 = [0] * a0
    a3 = 0
    b = l1(b)
    for n in range(len(b)):
        a1[a3] = l3(256, b[n] + a1[a3])
        a3 += 1
        if a3 >= a0:
            a3 = 0
    return bytes(a1)







