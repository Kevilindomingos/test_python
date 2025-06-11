import pytest

@pytest.fixture
def Lista_simples():
    return [1, 2, 3, 4]

def test_somar(Lista_simples):
    assert sum(Lista_simples) == 10
    
def test_tamanho_lista(Lista_simples):
    assert len(Lista_simples) == 4
    
def test_tipo_estrutura(Lista_simples):
    assert type(Lista_simples) == list
    
def test_numero_maximo(Lista_simples):
    assert max(Lista_simples) == 4