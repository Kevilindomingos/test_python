import requests
from unittest.mock import MagicMock
import pytest

@pytest.fixture

def buscar_resposta_mock():
    
    mock = MagicMock(spec=requests.Response)
    mock.status_code = 200
    mock. json.return_value = {'Mensagem' : 'Acesso com sucesso'}
    return mock

def test_conferencia_resposta_mock(buscar_resposta_mock):
    resposta = buscar_resposta_mock
    assert resposta.status_code == 200
    assert resposta.json() == {'Mensagem' : 'Acesso com sucesso'}