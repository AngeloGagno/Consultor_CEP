import requests


class CEP_API:
    """Realiza a requisição à API"""
    
    def get_CEP(self, UF:str,CITY:str, ADD:str):
        '''UF: Estado Abreviado\n
        CITY:Cidade\n
        ADD: Endereço(Logradouro)
        '''
        """Endpoint CEP"""
        response = requests.get(f'https://viacep.com.br/ws/{UF}/{CITY}/{ADD}/json/')
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def get_address(self, CEP:int):
        '''CEP: Número do CEP
        '''
        """Endpoint Address"""
        response = requests.get(f'https://viacep.com.br/ws/{CEP}/json/')  
        if response.status_code == 200:
            return response.json()
        else:
            return None