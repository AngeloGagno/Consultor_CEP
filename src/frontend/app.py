import streamlit as st
from backend.backend import DataModel

class Webpage:
    def __init__(self):
        """Inicializa a interface do usuário."""
        self.data_model = DataModel() 
        self.setup_ui()

    def setup_ui(self):
        """Configura a interface inicial."""
        self.show_title()
        self.show_subtitle()
        self.request_type = self.select_request_type()
        self.handle_request()

    def show_title(self):
        """Exibe o título da aplicação com estilo personalizado."""
        st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Verificador de CEP</h1>", unsafe_allow_html=True)

    def show_subtitle(self):
        """Exibe o subtítulo da aplicação com estilo personalizado."""
        st.markdown("<h3 style='text-align: center; color: #3e8e41;'>Selecione o tipo de requisição</h3>", unsafe_allow_html=True)

    def select_request_type(self):
        """Permite ao usuário selecionar o tipo de consulta (CEP ou Endereço)."""
        return st.selectbox(
            'Formato de envio de dados',
            ['CEP', 'Endereço'],
            index=0,
            key='request_type',
            help="Escolha entre procurar por CEP ou Endereço"
        )

    def get_state_selection(self):
        """Exibe um selectbox para seleção de estado."""
        estados = [
            "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", 
            "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", 
            "RR", "SC", "SP", "SE", "TO"
        ]
        return st.selectbox('Selecione um estado', estados, key='state')

    def get_text_input(self, label):
        """Exibe um campo de entrada de texto com estilo."""
        return st.text_input(label, key=label)

    def submit_button(self):
        """Cria um botão de envio com estilo customizado."""
        return st.button('Enviar dados', key='submit', help="Clique para enviar seus dados")

    def create_cep_json(self, cep):
        """Cria um dicionário JSON para consulta de CEP."""
        return {'CEP': cep}

    def create_address_json(self, state, city, address):
        """Cria um dicionário JSON para consulta de endereço."""
        return {'Address': address, 'UF': state, 'City': city}

    def handle_request(self):
        """Gerencia a requisição de CEP ou Endereço."""
        if self.request_type == 'Endereço':
            self.handle_address_request()
        elif self.request_type == 'CEP':
            self.handle_cep_request()

    def handle_address_request(self):
        """Processa a consulta por endereço."""
        state = self.get_state_selection()
        city = self.get_text_input('Digite a cidade')
        address = self.get_text_input('Digite o endereço')

        if self.submit_button():
            if not all([state, city, address]):
                st.error('Preencha todos os campos corretamente.')
                return

            address_json = self.create_address_json(state, city, address)
            response = self.data_model.connect_frontend(address_json)

            if 'error' in response:
                st.error(f"Erro: {response['error']}")
            else:
                st.success(f"CEP encontrado: {response['api_response']['cep']}")

    def handle_cep_request(self):
        """Processa a consulta por CEP."""
        cep = self.get_text_input('Digite o CEP do local')

        if self.submit_button():
            if not cep:
                st.error('Preencha o campo do CEP corretamente.')
                return

            cep_json = self.create_cep_json(cep)
            response = self.data_model.connect_frontend(cep_json)

            if 'error' in response:
                st.error(f"Erro: {response['error']}")
            elif 'erro' in response['api_response']:
                st.error('Insira um CEP válido.')
            else:
                api_response = response['api_response']
                st.success(f"Endereço correspondente ao CEP: {api_response['logradouro']} - {api_response['bairro']}, {api_response['localidade']}/{api_response['uf']}")
