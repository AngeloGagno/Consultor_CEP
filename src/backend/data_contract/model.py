from pydantic import BaseModel,field_validator


class CEP(BaseModel):
    """Validador do CEP"""
    CEP:int

    @field_validator('CEP')
    def validar_cep(cls,v):
        if not (1000000 <= v <= 99999999):
            raise ValueError("O CEP deve ter exatamente 8 dígitos numéricos. Exemplo: 01001000")
        return v
    
class Address(BaseModel):
    """Validador dos parâmetros de endereço"""
    Address:str
    UF:str
    City:str

