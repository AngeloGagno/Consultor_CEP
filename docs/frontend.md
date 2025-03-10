# Estrutura do Frontend

## Introdução
Este documento descreve a interface do usuário desenvolvida em **Streamlit** para o **Verificador de CEP**. A aplicação permite realizar consultas de **CEP** e **endereço** utilizando a API do **ViaCEP**.

---

## Estrutura da Classe `Webpage`
A classe `Webpage` é responsável por gerenciar a interface do usuário e suas interações.

```python
 def __init__(self):
     """Inicializa a interface do usuário."""
     self.data_model = DataModel()
     self.setup_ui()
```

### `setup_ui(self)`
Monta a estrutura da interface do usuário, incluindo títulos e menus.

```python
 def setup_ui(self):
     """Configura a interface inicial."""
     self.show_title()
     self.show_subtitle()
     self.request_type = self.select_request_type()
     self.handle_request()
```

### `select_request_type(self)`
Cria um **selectbox** para que o usuário escolha entre consulta por **CEP** ou **Endereço**.

```python
 def select_request_type(self):
     """Permite ao usuário selecionar o tipo de consulta."""
     return st.selectbox(
         'Formato de envio de dados',
         ['CEP', 'Endereço'],
         index=0,
         key='request_type',
         help="Escolha entre procurar por CEP ou Endereço"
     )
```

### `get_state_selection(self)`
Cria um menu suspenso para seleção do estado (**UF**).

```python
 def get_state_selection(self):
     """Exibe um selectbox para seleção de estado."""
     estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
     return st.selectbox('Selecione um estado', estados, key='state')
```

### `get_text_input(self, label)`
Cria um campo de entrada de texto.

```python
 def get_text_input(self, label):
     """Exibe um campo de entrada de texto."""
     return st.text_input(label, key=label)
```

### `submit_button(self)`
Cria um botão para envio dos dados inseridos pelo usuário.

```python
 def submit_button(self):
     """Cria um botão de envio."""
     return st.button('Enviar dados', key='submit', help="Clique para enviar seus dados")
```

### `create_cep_json(self, cep)`
Gera um dicionário no formato JSON para consulta de **CEP**.

```python
 def create_cep_json(self, cep):
     """Cria um dicionário JSON para consulta de CEP."""
     return {'CEP': cep}
```

### `create_address_json(self, state, city, address)`
Gera um dicionário no formato JSON para consulta de **endereço**.

```python
 def create_address_json(self, state, city, address):
     """Cria um dicionário JSON para consulta de endereço."""
     return {'Address': address, 'UF': state, 'City': city}
```

### `handle_request(self)`
Gerencia o tipo de requisição selecionada (CEP ou Endereço) e chama o método correspondente.

```python
 def handle_request(self):
     """Gerencia a requisição de CEP ou Endereço."""
     if self.request_type == 'Endereço':
         self.handle_address_request()
     elif self.request_type == 'CEP':
         self.handle_cep_request()
```

### `handle_address_request(self)`
Realiza a consulta por **endereço**.

```python
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
```

### `handle_cep_request(self)`
Realiza a consulta por **CEP**.

```python
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
```

