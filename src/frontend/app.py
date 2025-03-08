import streamlit as st

class Webpage:
    def __init__(self):
        self.title()
        self.subtitle()
        self.condition = self.select_box()  # Armazena a escolha do usuário
        self.fetch_all()

    def title(self):
        st.title('Verificador de CEP')
    
    def subtitle(self):
        st.markdown('## Selecione o tipo de requisição')

    def select_box(self):
        return st.selectbox('Formato de envio de dados', ['CEP', 'Endereço'], placeholder='Selecione um formato')

    def select_state(self):
        estados = [
            "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", 
            "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", 
            "RR", "SC", "SP", "SE", "TO"
        ]
        return st.selectbox('Selecione um estado', estados)

    def address_information(self, info):
        return st.text_input(info)

    def submit_button(self):
        return st.button('Enviar dados')

    def fetch_all(self):
        if self.condition == 'Endereço':
            state = self.select_state()
            address = self.address_information('Digite o endereço do local')
            if self.submit_button():
                st.write(f"Endereço selecionado: {address}-{state}")
                return address,state
        elif self.condition == 'CEP':
            cep = self.address_information('Digite o CEP do local')
            if self.submit_button():
                st.write(f"CEP informado: {cep}")
                return cep
if __name__ == '__main__':
    Webpage()
