# Estrutura do Projeto
## Estrutura do Projeto em pastas

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
