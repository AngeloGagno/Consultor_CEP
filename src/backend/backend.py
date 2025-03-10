from backend.request.api import CEP_API
from backend.data_contract.model import CEP, Address
from pydantic import ValidationError

class DataModel:
    def __init__(self):
        """Inicializa a API de consulta de CEP."""
        self.api = CEP_API()

    def validate_cep(self, cep_info):
        """Valida o formato do CEP usando Pydantic."""
        try:
            cep_info['CEP'] = cep_info['CEP'].replace('-','')
            return CEP(**cep_info)
        except ValidationError:
            return {"error": "CEP inválido! Digite um número de 8 dígitos."}

    def validate_address(self, address_info):
        """Valida o formato do endereço usando Pydantic."""
        try:
            return Address(**address_info)
        except ValidationError:
            return {"error": "Endereço inválido! Certifique-se de preencher corretamente os campos."}

    def handle_cep_request(self, data):
        """Processa a requisição para busca por CEP."""
        validated_data = self.validate_cep(data)

        if "error" in validated_data:
            return validated_data  # Retorna erro se a validação falhar

        response = self.api.get_address(validated_data.CEP)
        return {
            "validated": validated_data.dict(),
            "api_response": response if response else {"error": "Não foi possível obter informações para este CEP."}
        }

    def handle_address_request(self, data):
        """Processa a requisição para busca por endereço."""
        validated_data = self.validate_address(data)

        if "error" in validated_data:
            return validated_data  # Retorna erro se a validação falhar

        response = self.api.get_CEP(
            validated_data.UF, validated_data.City, validated_data.Address
        )

        return {
            "validated": validated_data.dict(),
            "api_response": response[0] if response else "Não foi possível obter informações para este endereço."
        }

    def connect_frontend(self, data: dict):
        """Valida os dados recebidos e direciona para a consulta correta."""

        if "Address" in data:
            return self.handle_address_request(data)
        elif "CEP" in data:
            return self.handle_cep_request(data)
        else:
            return {
                "error": "Formato inválido!."
            }

