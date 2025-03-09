import pytest
import requests
import requests_mock
from backend.request.api import CEP_API


@pytest.fixture
def api():
    return CEP_API()


def test_get_CEP_success(api):
    """Testa a busca de CEP por UF e endereço com sucesso"""
    uf = "SP"
    endereco = "Sao Paulo/Avenida Paulista"

    with requests_mock.Mocker() as m:
        mock_response = [{"cep": "01311-000", "logradouro": "Avenida Paulista", "bairro": "Bela Vista"}]
        m.get(f'https://viacep.com.br/ws/{uf}/{endereco}/json/', json=mock_response, status_code=200)

        response = api.get_CEP(uf, endereco)
        assert response == mock_response


def test_get_CEP_failure(api):
    """Testa a falha na busca de CEP"""
    uf = "SP"
    endereco = "EnderecoInvalido"

    with requests_mock.Mocker() as m:
        m.get(f'https://viacep.com.br/ws/{uf}/{endereco}/json/', status_code=404)

        response = api.get_CEP(uf, endereco)
        assert response is None


def test_get_address_success(api):
    """Testa a busca de endereço por CEP com sucesso"""
    cep = "01311-000"

    with requests_mock.Mocker() as m:
        mock_response = {"cep": "01311-000", "logradouro": "Avenida Paulista", "bairro": "Bela Vista"}
        m.get(f'https://viacep.com.br/ws/{cep}/json/', json=mock_response, status_code=200)

        response = api.get_address(cep)
        assert response == mock_response


def test_get_address_failure(api):
    """Testa a falha na busca de endereço por CEP"""
    cep = "00000-000"

    with requests_mock.Mocker() as m:
        m.get(f'https://viacep.com.br/ws/{cep}/json/', status_code=404)

        response = api.get_address(cep)
        assert response is None
