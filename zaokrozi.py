import numpy as np
import math


def zaok(a):
    v = a[0]
    dv = a[1]

    dn = vodilna_stevka(dv)

    dv_o = zaokrozevalnik(dn, dv)

    dn = vodilna_stevka(dv_o)

    v_o = zaokrozevalnik(dn, v)

    return np.array((v_o, dv_o))


def vodilna_stevka(v):
    n = np.log10(v)
    n = math.floor(n)

    return n

def zaokrozevalnik(n, v):
    if n > 0:
        glavna = math.floor(v/(10**n))*10**n

        druga = v - glavna
        druga = math.floor(druga/(10**(n-1)))

        if druga >= 5:
            glavna += 1*10**n

    else:
        glavna = round(v, -n)

    return glavna
