from funcoes import *

def test_verifSenha():
    assert validar_senha('senha123!') == 'senha cadastrada'
    assert validar_senha('senha123') == 'senha não cadastrada'
    assert validar_senha('SENHA123@') == 'senha cadastrada'
    assert validar_senha('senh@a') == 'senha não cadastrada'
    
def test_calcMedia():
    assert calcular_media([7, 7, 7, 7]) == 7.0
    assert calcular_media([]) == 0
    
def test_verif_maiorIdade():
    assert verif_maiorIdade(18) == True
    assert verif_maiorIdade(17) == True
    assert verif_maiorIdade(19) == False
    
def test_numPositivo():
    assert numPositivo(5) == 'positivo'
    assert numPositivo(0) == 'positivo'
    assert numPositivo(-1) == 'negativo'
    
def test_mediaAluno():
    assert status_aluno(2.5) == 'reprovado'
    assert status_aluno(5.0) == 'recuperação'
    assert status_aluno(7.5) == 'aprovado'
    assert status_aluno(3.0) == 'recuperação'