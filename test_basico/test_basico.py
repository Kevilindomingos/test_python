def par(numero):
    if numero % 2 == 0:
        return 'é par!'
    else: 
        return 'é ímpar!'
def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def test_numPar():
    assert par(5) == 'é ímpar!'
    assert par(6) == 'é par!'
    
def test_somaSubtrair():
    assert somar(5,6) == 11
    assert subtrair(10,8) == 2