




#a3a4a0a5

def l1(b):
    return list(b)

def l2(b):
    return bytes(b)

def l3(m, n):
    while n < 0 or n >= m:
        if n < 0:
            n += m
        if n >= m:
            n -= m
    return n

def l0(code, key, command):
    if command:
        command = 1
    else:
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
    return l2(code)



def c1(p, i, n):
    return l3(p, i ** n)

def p1(n):
    r = int(n ** 0.5)
    if n == 2:
        return False
    for v in range(2, r + 1):
        if n % v == 0:
            return False
    return True

def b1(n):
    v = ''
    while n > 0:
        n1 = n / 2
        if n1 == int(n1):
            v += '0'
        else:
            v += '1'
        n = int(n1)
    return v


def b2(b):
    s1 = 0
    for n in range(8):
        s1 += 2 ** n * int(b[n])
    return s1

def b3(l):
    b = ''
    l1 = len(l)
    for n in range(8):
        if n >= l1:
            b += '0'
        else:
            b += l[n]
    return b

def b4(b):
    s0 = []
    while b:
        s0.append(b2(b3(b)))
        b = b[8:]    
    return s0

def b0(n):
    return b4(b1(n))




def h0(b):
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







