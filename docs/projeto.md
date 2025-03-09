# Estrutura do Projeto
## Estrutura do Projeto em pastas
    mkdocs.yml          
    docs/
        └── index.md     
    src/
        ├── backend/       
        │   ├── data_contract/
        │   │   └── model.py   
        │   ├── request/
        │   │   └── api.py     
        │   └── backend.py     
        ├── frontend/     
        │   └── app.py    
        ├── tests/         
        │   ├── api_tests.py   
        │   └── frontend_tests.py 
        └── main.py        

### Descrição das pastas e arquivos:

- **mkdocs.yml**: Configuração do MkDocs para gerar a documentação do projeto.
- **docs/index.md**: Página inicial da documentação do projeto, com informações gerais e guias de uso.
- **backend/data_contract/model.py**: Define os modelos de dados e contratos utilizados pelo sistema, garantindo a validação e consistência dos dados.
- **backend/request/api.py**: Responsável pelas chamadas de API, realizando as requisições aos endpoints e tratando as respostas.
- **backend/backend.py**: Contém a lógica de processamento de dados do backend e orquestra as operações do sistema.
- **frontend/app.py**: Código responsável pela interface de usuário do sistema, com as interações no frontend.
- **tests/api_tests.py**: Testes unitários que validam o comportamento das funções relacionadas à API.
- **tests/frontend_tests.py**: Testes unitários que verificam a interação e o funcionamento do frontend.
- **main.py**: Ponto de entrada principal da aplicação, responsável por iniciar e rodar a interface do sistema.

## Descrevendo as Classes e Funções

### backend/data_contract/model.py

#### Validação de CEP e Endereço

# 📌 Documentação do Sistema de Consulta de CEP

## 📖 Visão Geral

Este sistema realiza a consulta de **endereços a partir do CEP** e **CEPs a partir do endereço**, utilizando a API do **ViaCEP**.

---

## 📌 Estrutura do Projeto

```
📂 backend/
    📂 data_contract/
        📜 model.py    	# Modelos para validação de CEP e Endereço
    📂 request/
        📜 api.py       	# Conexão com a API ViaCEP
    📜 backend.py     	# Operações principais do backend
📂 frontend/
    📜 app.py         	# Interface do sistema com Streamlit
📂 tests/
    📜 api_tests.py   	# Testes para a API
    📜 frontend_tests.py # Testes da interface
📜 main.py          	# Executa a aplicação
```

---

## 📌 Modelos de Dados (`backend/data_contract/model.py`)

Os modelos abaixo utilizam **Pydantic** para validar os dados de entrada do sistema.

### 🔹 `Classe CEP`

```python
class CEP(BaseModel):
    """Validador do CEP"""
    CEP: int

    @field_validator('CEP')
    def validar_cep(cls, v):
        if not (1000000 <= v <= 99999999):
            raise ValueError("O CEP deve ter exatamente 8 dígitos numéricos.")
        return v
```

### 🔹 `Classe Address`

```python
class Address(BaseModel):
    """Validador dos parâmetros de endereço"""
    Address: str
    UF: str
    City: str
```

---

## 📌 API de Consulta (`backend/request/api.py`)

### 🔹 `Classe CEP_API`

Esta classe realiza as requisições para a API do **ViaCEP**.

#### 🔸 `get_CEP(UF, CITY, ADD)`

```python
def get_CEP(self, UF: str, CITY: str, ADD: str):
```

- **Entrada**:
    - `UF`: Sigla do estado
    - `CITY`: Nome da cidade
    - `ADD`: Nome da rua
- **Saída**:
    - JSON com a lista de CEPs correspondentes
    - `None` se a consulta falhar

#### 🔸 `get_address(CEP)`

```python
def get_address(self, CEP: int):
```

- **Entrada**:
    - `CEP`: Número do CEP
- **Saída**:
    - JSON com os dados do endereço correspondente
    - `None` se a consulta falhar

---

## 📌 Processamento de Dados (`backend/backend.py`)

### 🔹 `Classe DataModel`

Gerencia a **validação e consulta** de **CEP** e **endereço**.

```python
class DataModel:
    def __init__(self):
        self.api = CEP_API()
```

### 🔸 `validate_cep(cep_info)`

```python
def validate_cep(self, cep_info):
```

- **Valida** um CEP com Pydantic
- **Entrada**: `dict` com um CEP
- **Saída**:
    - ✅ Se válido: Objeto `CEP`
    - ❌ Se inválido: `{ "error": "CEP inválido!" }`

### 🔸 `validate_address(address_info)`

```python
def validate_address(self, address_info):
```

- **Valida** um endereço com Pydantic
- **Entrada**: `dict` com **UF, cidade e logradouro**
- **Saída**:
    - ✅ Se válido: Objeto `Address`
    - ❌ Se inválido: `{ "error": "Endereço inválido!" }`

### 🔸 `handle_cep_request(data)`

```python
def handle_cep_request(self, data):
```

- **Processa** a consulta de endereço por CEP
- **Entrada**: `dict` com o CEP
- **Saída**:
    - ✅ `{ "api_response": {dados do endereço} }`
    - ❌ `{ "error": "CEP inválido!" }`

### 🔸 `handle_address_request(data)`

```python
def handle_address_request(self, data):
```

- **Processa** a consulta de CEP por endereço
- **Entrada**: `dict` com **UF, cidade e logradouro**
- **Saída**:
    - ✅ `{ "api_response": {dados do CEP} }`
    - ❌ `{ "error": "Endereço inválido!" }`

### 🔸 `connect_frontend(data)`

```python
def connect_frontend(self, data: dict):
```

- **Direciona** a requisição para o método correto
- **Entrada**: `dict` com **CEP** ou **endereço**
- **Saída**:
    - ✅ Resultado da API
    - ❌ `{ "error": "Formato inválido!" }`

---

## 📌 Exemplo de Uso

```python
modelo = DataModel()

# Busca por CEP
cep_data = {"CEP": "01001000"}
resultado_cep = modelo.connect_frontend(cep_data)
print(resultado_cep)

# Busca por Endereço
endereco_data = {"UF": "SP", "City": "São Paulo", "Address": "Praça da Sé"}
resultado_endereco = modelo.connect_frontend(endereco_data)
print(resultado_endereco)
```


