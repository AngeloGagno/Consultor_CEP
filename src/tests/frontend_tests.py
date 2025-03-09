import pytest
from streamlit.testing.v1 import AppTest
from frontend.app import Webpage

def test_webpage():
    app = AppTest(Webpage, default_timeout=10) 
    app.run()
    assert app.title == "Verificador de CEP"
    assert "Selecione o tipo de requisição" in app.markdown[0].value
    assert app.selectbox[0].label == "Formato de envio de dados"

    # Simulando seleção de 'Endereço' no selectbox
    app.selectbox[0].set_value("Endereço")
    app.run()

    # Verifica se o estado e campo de endereço aparecem
    assert app.selectbox[1].label == "Selecione um estado"
    assert app.text_input[0].label == "Digite o endereço do local"

    # Simulando entrada de dados e clique no botão
    app.text_input[0].set_value("Rua Exemplo, 123")
    app.selectbox[1].set_value("SP")
    app.button[0].click()
    app.run()

    # Verifica se os dados foram enviados corretamente
    assert "Endereço selecionado: Rua Exemplo, 123-SP" in app.markdown[1].value

    # Simulando seleção de 'CEP' no selectbox
    app.selectbox[0].set_value("CEP")
    app.run()

    # Verifica se o campo de CEP aparece
    assert app.text_input[0].label == "Digite o CEP do local"

    # Simulando entrada de um CEP e clique no botão
    app.text_input[0].set_value("01001-000")
    app.button[0].click()
    app.run()

    # Verifica se o CEP foi enviado corretamente
    assert "CEP informado: 01001-000" in app.markdown[1].value


if __name__ == "__main__":
    pytest.main()